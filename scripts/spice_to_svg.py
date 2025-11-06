#!/usr/bin/env python3
"""
SPICE to SVG Schematic Generator
Converts SPICE netlists to visual circuit schematics in SVG format
"""

import re
import sys
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass
import xml.etree.ElementTree as ET
from xml.dom import minidom


@dataclass
class Component:
    """Represents an electronic component"""
    name: str  # e.g., R1, C1, Q1
    type: str  # e.g., 'R', 'C', 'L', 'Q', 'D'
    value: str  # e.g., '10k', '100uF'
    nodes: List[str]  # Connection nodes


@dataclass
class Connection:
    """Represents a connection between components"""
    node: str
    components: List[Tuple[str, int]]  # (component_name, pin_index)


class SPICEParser:
    """Parses SPICE netlists"""
    
    COMPONENT_TYPES = {
        'R': 'Resistor',
        'C': 'Capacitor',
        'L': 'Inductor',
        'D': 'Diode',
        'Q': 'BJT',
        'M': 'MOSFET',
        'V': 'Voltage Source',
        'I': 'Current Source',
    }
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.components: Dict[str, Component] = {}
        self.connections: Dict[str, Connection] = {}
        self.title = "Circuit Schematic"
        
    def parse(self) -> Tuple[Dict[str, Component], Dict[str, Connection]]:
        """Parse SPICE netlist file"""
        try:
            with open(self.filepath, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Error: File '{self.filepath}' not found")
            sys.exit(1)
        
        for line in lines:
            line = line.strip()
            
            # Skip comments and empty lines
            if not line or line.startswith('*') or line.startswith('.'):
                continue
            
            # Parse title
            if line.upper().startswith('TITLE') or line.upper().startswith('.TITLE'):
                self.title = line.split(maxsplit=1)[1] if len(line.split(maxsplit=1)) > 1 else "Circuit"
                continue
            
            # Parse component lines
            self._parse_component_line(line)
        
        # Build connection map
        self._build_connections()
        
        return self.components, self.connections
    
    def _parse_component_line(self, line: str):
        """Parse a single component line"""
        parts = line.split()
        if not parts:
            return
        
        comp_name = parts[0]
        comp_type = comp_name[0].upper()
        
        if comp_type not in self.COMPONENT_TYPES:
            return
        
        # Format: <NAME> <NODE1> [<NODE2> ...] <VALUE>
        if len(parts) < 3:
            return
        
        # For resistors, capacitors, inductors: R1 GND OUT 10k
        if comp_type in ['R', 'C', 'L']:
            nodes = parts[1:-1]
            value = parts[-1]
            self.components[comp_name] = Component(comp_name, comp_type, value, nodes)
        
        # For diodes: D1 ANODE CATHODE
        elif comp_type == 'D':
            nodes = parts[1:3]
            value = parts[-1] if len(parts) > 3 else "1N4148"
            self.components[comp_name] = Component(comp_name, comp_type, value, nodes)
        
        # For BJTs: Q1 C B E <model>
        elif comp_type == 'Q':
            nodes = parts[1:4]
            value = parts[4] if len(parts) > 4 else "2N2222"
            self.components[comp_name] = Component(comp_name, comp_type, value, nodes)
        
        # For MOSFETs: M1 D G S B <model>
        elif comp_type == 'M':
            nodes = parts[1:5]
            value = parts[5] if len(parts) > 5 else "NMOS"
            self.components[comp_name] = Component(comp_name, comp_type, value, nodes)
        
        # For sources: V1 + - DC 5V
        elif comp_type in ['V', 'I']:
            nodes = parts[1:3]
            value = ' '.join(parts[3:]) if len(parts) > 3 else "DC 0"
            self.components[comp_name] = Component(comp_name, comp_type, value, nodes)
    
    def _build_connections(self):
        """Build connection map from components"""
        for comp_name, comp in self.components.items():
            for pin_idx, node in enumerate(comp.nodes):
                if node not in self.connections:
                    self.connections[node] = Connection(node, [])
                self.connections[node].components.append((comp_name, pin_idx))


class SchematicRenderer:
    """Renders circuit schematic to SVG"""
    
    COMPONENT_SYMBOLS = {
        'R': 'resistor',
        'C': 'capacitor',
        'L': 'inductor',
        'D': 'diode',
        'Q': 'bjt',
        'M': 'mosfet',
        'V': 'voltage_source',
        'I': 'current_source',
    }
    
    def __init__(self, components: Dict[str, Component], connections: Dict[str, Connection], title: str = "Circuit"):
        self.components = components
        self.connections = connections
        self.title = title
        self.width = 1200
        self.height = 800
        self.margin = 50
        self.grid_size = 100
        self.component_ports: Dict[str, Dict[int, Tuple[int, int]]] = {}  # Track component port positions
        
    def render(self, output_file: str):
        """Render schematic to SVG file"""
        root = ET.Element('svg', {
            'xmlns': 'http://www.w3.org/2000/svg',
            'viewBox': f'0 0 {self.width} {self.height}',
            'width': str(self.width),
            'height': str(self.height)
        })
        
        # Add style
        style = ET.SubElement(root, 'style')
        style.text = """
        .component-text { font-family: Arial, sans-serif; font-size: 12px; fill: #333; }
        .node-label { font-family: Arial, sans-serif; font-size: 10px; fill: #666; }
        .wire { stroke: #000; stroke-width: 2; fill: none; }
        .connection { fill: #000; radius: 3; }
        .title { font-family: Arial, sans-serif; font-size: 18px; font-weight: bold; fill: #000; }
        """
        
        # Add title
        title_elem = ET.SubElement(root, 'text', {
            'x': str(self.margin),
            'y': str(self.margin),
            'class': 'title'
        })
        title_elem.text = self.title
        
        # Calculate component positions
        positions = self._calculate_positions()
        
        # Draw components
        y_pos = self.margin + 60
        col = 0
        row = 0
        
        for comp_name, comp in sorted(self.components.items()):
            x_pos = self.margin + 100 + (col * 250)
            if x_pos + 100 > self.width - self.margin:
                col = 0
                row += 1
                x_pos = self.margin + 100
            
            y_pos = self.margin + 100 + (row * 200)
            positions[comp_name] = (x_pos, y_pos)
            
            self._draw_component(root, comp, x_pos, y_pos)
            col += 1
        
        # Create a group for wires (drawn first so they appear behind components)
        wires_group = ET.Element('g', {'id': 'wires'})
        root.insert(len(root) - 1, wires_group)  # Insert before components
        
        # Draw connections
        self._draw_connections(wires_group, positions)
        
        # Pretty print and save
        xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
        xml_str = '\n'.join(xml_str.split('\n')[1:])  # Remove XML declaration
        
        with open(output_file, 'w') as f:
            f.write(xml_str)
        
        print(f"Schematic saved to: {output_file}")
    
    def _calculate_positions(self) -> Dict[str, Tuple[int, int]]:
        """Calculate component positions"""
        return {}
    
    def _draw_component(self, parent: ET.Element, comp: Component, x: int, y: int):
        """Draw a single component"""
        group = ET.SubElement(parent, 'g', {'id': comp.name})
        
        # Initialize port tracking for this component
        self.component_ports[comp.name] = {}
        
        # Draw component symbol
        if comp.type == 'R':
            self._draw_resistor(group, x, y, comp.name)
        elif comp.type == 'C':
            self._draw_capacitor(group, x, y, comp.name)
        elif comp.type == 'L':
            self._draw_inductor(group, x, y, comp.name)
        elif comp.type == 'D':
            self._draw_diode(group, x, y, comp.name)
        elif comp.type == 'Q':
            self._draw_bjt(group, x, y, comp.name)
        elif comp.type == 'M':
            self._draw_mosfet(group, x, y, comp.name)
        elif comp.type == 'V':
            self._draw_voltage_source(group, x, y, comp.name)
        elif comp.type == 'I':
            self._draw_current_source(group, x, y, comp.name)
        
        # Draw label
        label = ET.SubElement(group, 'text', {
            'x': str(x),
            'y': str(y + 50),
            'text-anchor': 'middle',
            'class': 'component-text'
        })
        label.text = f"{comp.name}\n{comp.value}"
    
    def _draw_resistor(self, group: ET.Element, x: int, y: int, comp_name: str = None):
        """Draw resistor symbol"""
        # Draw rectangle
        rect = ET.SubElement(group, 'rect', {
            'x': str(x - 25),
            'y': str(y - 10),
            'width': '50',
            'height': '20',
            'fill': 'none',
            'stroke': '#000',
            'stroke-width': '2'
        })
        
        # Draw connection lines
        line1 = ET.SubElement(group, 'line', {
            'x1': str(x - 40),
            'y1': str(y),
            'x2': str(x - 25),
            'y2': str(y),
            'class': 'wire'
        })
        line2 = ET.SubElement(group, 'line', {
            'x1': str(x + 25),
            'y1': str(y),
            'x2': str(x + 40),
            'y2': str(y),
            'class': 'wire'
        })
        
        # Track port positions
        if comp_name:
            self.component_ports[comp_name][0] = (x - 40, y)
            self.component_ports[comp_name][1] = (x + 40, y)
    
    def _draw_capacitor(self, group: ET.Element, x: int, y: int, comp_name: str = None):
        """Draw capacitor symbol"""
        # Draw two parallel lines
        line1 = ET.SubElement(group, 'line', {
            'x1': str(x - 10),
            'y1': str(y - 15),
            'x2': str(x - 10),
            'y2': str(y + 15),
            'stroke': '#000',
            'stroke-width': '2'
        })
        line2 = ET.SubElement(group, 'line', {
            'x1': str(x + 10),
            'y1': str(y - 15),
            'x2': str(x + 10),
            'y2': str(y + 15),
            'stroke': '#000',
            'stroke-width': '2'
        })
        
        # Draw connection lines
        line3 = ET.SubElement(group, 'line', {
            'x1': str(x - 40),
            'y1': str(y),
            'x2': str(x - 10),
            'y2': str(y),
            'class': 'wire'
        })
        line4 = ET.SubElement(group, 'line', {
            'x1': str(x + 10),
            'y1': str(y),
            'x2': str(x + 40),
            'y2': str(y),
            'class': 'wire'
        })
        
        # Track port positions
        if comp_name:
            self.component_ports[comp_name][0] = (x - 40, y)
            self.component_ports[comp_name][1] = (x + 40, y)
    
    def _draw_inductor(self, group: ET.Element, x: int, y: int, comp_name: str = None):
        """Draw inductor symbol (coil)"""
        # Draw coil loops
        for i in range(4):
            arc = ET.SubElement(group, 'path', {
                'd': f'M {x - 30 + i*15} {y} Q {x - 22 + i*15} {y - 10} {x - 15 + i*15} {y}',
                'fill': 'none',
                'stroke': '#000',
                'stroke-width': '2'
            })
        
        # Draw connection lines
        line1 = ET.SubElement(group, 'line', {
            'x1': str(x - 40),
            'y1': str(y),
            'x2': str(x - 30),
            'y2': str(y),
            'class': 'wire'
        })
        line2 = ET.SubElement(group, 'line', {
            'x1': str(x + 30),
            'y1': str(y),
            'x2': str(x + 40),
            'y2': str(y),
            'class': 'wire'
        })
        
        # Track port positions
        if comp_name:
            self.component_ports[comp_name][0] = (x - 40, y)
            self.component_ports[comp_name][1] = (x + 40, y)
    
    def _draw_diode(self, group: ET.Element, x: int, y: int, comp_name: str = None):
        """Draw diode symbol"""
        # Draw triangle and line
        polygon = ET.SubElement(group, 'polygon', {
            'points': f'{x},{y-10} {x-20},{y+10} {x+20},{y+10}',
            'fill': 'none',
            'stroke': '#000',
            'stroke-width': '2'
        })
        line = ET.SubElement(group, 'line', {
            'x1': str(x + 20),
            'y1': str(y - 10),
            'x2': str(x + 20),
            'y2': str(y + 10),
            'stroke': '#000',
            'stroke-width': '2'
        })
        
        # Connection lines
        line3 = ET.SubElement(group, 'line', {
            'x1': str(x - 40),
            'y1': str(y),
            'x2': str(x - 20),
            'y2': str(y),
            'class': 'wire'
        })
        line4 = ET.SubElement(group, 'line', {
            'x1': str(x + 20),
            'y1': str(y),
            'x2': str(x + 40),
            'y2': str(y),
            'class': 'wire'
        })
        
        # Track port positions
        if comp_name:
            self.component_ports[comp_name][0] = (x - 40, y)  # Anode
            self.component_ports[comp_name][1] = (x + 40, y)  # Cathode
    
    def _draw_bjt(self, group: ET.Element, x: int, y: int, comp_name: str = None):
        """Draw BJT symbol"""
        # Draw base line
        line1 = ET.SubElement(group, 'line', {
            'x1': str(x - 20),
            'y1': str(y - 15),
            'x2': str(x - 20),
            'y2': str(y + 15),
            'stroke': '#000',
            'stroke-width': '2'
        })
        
        # Draw collector and emitter lines
        line2 = ET.SubElement(group, 'line', {
            'x1': str(x - 20),
            'y1': str(y - 10),
            'x2': str(x + 15),
            'y2': str(y - 20),
            'stroke': '#000',
            'stroke-width': '2'
        })
        line3 = ET.SubElement(group, 'line', {
            'x1': str(x - 20),
            'y1': str(y + 10),
            'x2': str(x + 15),
            'y2': str(y + 20),
            'stroke': '#000',
            'stroke-width': '2'
        })
        
        # Connection lines (C, B, E)
        line4 = ET.SubElement(group, 'line', {
            'x1': str(x + 15),
            'y1': str(y - 20),
            'x2': str(x + 40),
            'y2': str(y - 20),
            'class': 'wire'
        })
        line5 = ET.SubElement(group, 'line', {
            'x1': str(x - 40),
            'y1': str(y),
            'x2': str(x - 20),
            'y2': str(y),
            'class': 'wire'
        })
        line6 = ET.SubElement(group, 'line', {
            'x1': str(x + 15),
            'y1': str(y + 20),
            'x2': str(x + 40),
            'y2': str(y + 20),
            'class': 'wire'
        })
        
        # Track port positions (C, B, E)
        if comp_name:
            self.component_ports[comp_name][0] = (x + 40, y - 20)  # Collector
            self.component_ports[comp_name][1] = (x - 40, y)       # Base
            self.component_ports[comp_name][2] = (x + 40, y + 20)  # Emitter
    
    def _draw_mosfet(self, group: ET.Element, x: int, y: int, comp_name: str = None):
        """Draw MOSFET symbol"""
        # Gate
        line1 = ET.SubElement(group, 'line', {
            'x1': str(x - 30),
            'y1': str(y - 15),
            'x2': str(x - 30),
            'y2': str(y + 15),
            'stroke': '#000',
            'stroke-width': '2'
        })
        
        # Channel
        rect = ET.SubElement(group, 'rect', {
            'x': str(x - 15),
            'y': str(y - 10),
            'width': '20',
            'height': '20',
            'fill': 'none',
            'stroke': '#000',
            'stroke-width': '2'
        })
        
        # Connection lines (D, G, S, B)
        line2 = ET.SubElement(group, 'line', {
            'x1': str(x - 5),
            'y1': str(y - 10),
            'x2': str(x - 5),
            'y2': str(y - 35),
            'class': 'wire'
        })
        line3 = ET.SubElement(group, 'line', {
            'x1': str(x - 5),
            'y1': str(y - 35),
            'x2': str(x + 40),
            'y2': str(y - 35),
            'class': 'wire'
        })
        line4 = ET.SubElement(group, 'line', {
            'x1': str(x - 40),
            'y1': str(y),
            'x2': str(x - 30),
            'y2': str(y),
            'class': 'wire'
        })
        line5 = ET.SubElement(group, 'line', {
            'x1': str(x - 5),
            'y1': str(y + 10),
            'x2': str(x - 5),
            'y2': str(y + 35),
            'class': 'wire'
        })
        line6 = ET.SubElement(group, 'line', {
            'x1': str(x - 5),
            'y1': str(y + 35),
            'x2': str(x + 40),
            'y2': str(y + 35),
            'class': 'wire'
        })
        
        # Track port positions (D, G, S, B)
        if comp_name:
            self.component_ports[comp_name][0] = (x + 40, y - 35)  # Drain
            self.component_ports[comp_name][1] = (x - 40, y)       # Gate
            self.component_ports[comp_name][2] = (x + 40, y + 35)  # Source
            self.component_ports[comp_name][3] = (x + 40, y + 35)  # Bulk
    
    def _draw_voltage_source(self, group: ET.Element, x: int, y: int, comp_name: str = None):
        """Draw voltage source (circle with +/-)"""
        circle = ET.SubElement(group, 'circle', {
            'cx': str(x),
            'cy': str(y),
            'r': '15',
            'fill': 'none',
            'stroke': '#000',
            'stroke-width': '2'
        })
        
        text = ET.SubElement(group, 'text', {
            'x': str(x),
            'y': str(y + 5),
            'text-anchor': 'middle',
            'class': 'component-text',
            'font-size': '16'
        })
        text.text = '~'
        
        # Connection lines
        line1 = ET.SubElement(group, 'line', {
            'x1': str(x - 40),
            'y1': str(y - 15),
            'x2': str(x - 15),
            'y2': str(y - 15),
            'class': 'wire'
        })
        line2 = ET.SubElement(group, 'line', {
            'x1': str(x - 15),
            'y1': str(y - 15),
            'x2': str(x),
            'y2': str(y - 15),
            'stroke': '#000',
            'stroke-width': '2'
        })
        line3 = ET.SubElement(group, 'line', {
            'x1': str(x),
            'y1': str(y - 15),
            'x2': str(x),
            'y2': str(y - 10),
            'stroke': '#000',
            'stroke-width': '2'
        })
        line4 = ET.SubElement(group, 'line', {
            'x1': str(x + 40),
            'y1': str(y + 15),
            'x2': str(x + 15),
            'y2': str(y + 15),
            'class': 'wire'
        })
        line5 = ET.SubElement(group, 'line', {
            'x1': str(x + 15),
            'y1': str(y + 15),
            'x2': str(x),
            'y2': str(y + 15),
            'stroke': '#000',
            'stroke-width': '2'
        })
        line6 = ET.SubElement(group, 'line', {
            'x1': str(x),
            'y1': str(y + 15),
            'x2': str(x),
            'y2': str(y + 10),
            'stroke': '#000',
            'stroke-width': '2'
        })
        
        # Track port positions
        if comp_name:
            self.component_ports[comp_name][0] = (x - 40, y - 15)  # Positive
            self.component_ports[comp_name][1] = (x + 40, y + 15)  # Negative
    
    def _draw_current_source(self, group: ET.Element, x: int, y: int, comp_name: str = None):
        """Draw current source (circle with arrow)"""
        circle = ET.SubElement(group, 'circle', {
            'cx': str(x),
            'cy': str(y),
            'r': '15',
            'fill': 'none',
            'stroke': '#000',
            'stroke-width': '2'
        })
        
        # Arrow inside
        arrow = ET.SubElement(group, 'polygon', {
            'points': f'{x},{y-5} {x+8},{y+3} {x-8},{y+3}',
            'fill': '#000'
        })
        
        # Connection lines
        line1 = ET.SubElement(group, 'line', {
            'x1': str(x - 40),
            'y1': str(y),
            'x2': str(x - 15),
            'y2': str(y),
            'class': 'wire'
        })
        line2 = ET.SubElement(group, 'line', {
            'x1': str(x + 15),
            'y1': str(y),
            'x2': str(x + 40),
            'y2': str(y),
            'class': 'wire'
        })
        
        # Track port positions
        if comp_name:
            self.component_ports[comp_name][0] = (x - 40, y)
            self.component_ports[comp_name][1] = (x + 40, y)
    
    def _draw_connections(self, parent: ET.Element, positions: Dict[str, Tuple[int, int]]):
        """Draw connection lines between components"""
        drawn_connections: Set[Tuple[Tuple[int, int], Tuple[int, int]]] = set()
        
        # Group connections by node
        for node, connection in self.connections.items():
            if len(connection.components) < 2:
                continue
            
            # Get all component ports connected to this node
            port_positions = []
            for comp_name, pin_idx in connection.components:
                if comp_name in self.component_ports and pin_idx in self.component_ports[comp_name]:
                    port_pos = self.component_ports[comp_name][pin_idx]
                    port_positions.append((comp_name, pin_idx, port_pos))
            
            # Draw connections between all ports on this node
            if len(port_positions) > 1:
                # Create a bus point (central connection point)
                x_coords = [pos[2][0] for pos in port_positions]
                y_coords = [pos[2][1] for pos in port_positions]
                
                bus_x = sum(x_coords) // len(x_coords)
                bus_y = sum(y_coords) // len(y_coords)
                
                # Draw lines from each port to the bus point
                for comp_name, pin_idx, (port_x, port_y) in port_positions:
                    # Create unique connection key to avoid duplicates
                    conn_key = tuple(sorted([(port_x, port_y), (bus_x, bus_y)]))
                    
                    if conn_key not in drawn_connections:
                        # Draw line with corner routing
                        path = ET.SubElement(parent, 'path', {
                            'd': f'M {port_x} {port_y} L {bus_x} {port_y} L {bus_x} {bus_y}',
                            'class': 'wire',
                            'stroke-linecap': 'round',
                            'stroke-linejoin': 'round'
                        })
                        drawn_connections.add(conn_key)
                
                # Draw node label at bus point
                node_label = ET.SubElement(parent, 'text', {
                    'x': str(bus_x + 5),
                    'y': str(bus_y - 10),
                    'class': 'node-label'
                })
                node_label.text = node
                
                # Draw connection dot
                dot = ET.SubElement(parent, 'circle', {
                    'cx': str(bus_x),
                    'cy': str(bus_y),
                    'r': '3',
                    'class': 'connection'
                })


def main():
    if len(sys.argv) < 2:
        print("Usage: python spice_to_svg.py <spice_file> [output_file.svg]")
        print("\nExample:")
        print("  python spice_to_svg.py circuit.cir")
        print("  python spice_to_svg.py circuit.cir schematic.svg")
        sys.exit(1)
    
    spice_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else spice_file.replace('.cir', '.svg').replace('.sp', '.svg')
    
    if not output_file.endswith('.svg'):
        output_file += '.svg'
    
    # Parse SPICE file
    parser = SPICEParser(spice_file)
    components, connections = parser.parse()
    
    if not components:
        print(f"Error: No components found in {spice_file}")
        sys.exit(1)
    
    print(f"Found {len(components)} components:")
    for name, comp in components.items():
        print(f"  {name}: {comp.type} {comp.value} nodes:{comp.nodes}")
    
    # Render schematic
    renderer = SchematicRenderer(components, connections, parser.title)
    renderer.render(output_file)


if __name__ == '__main__':
    main()
