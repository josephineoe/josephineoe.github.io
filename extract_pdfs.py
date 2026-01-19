import pdfplumber
import json

# PDF paths
pov_path = r"C:\Users\JosephineOE\Downloads\josephineoe.github.io-8a4babfcf759926128ab721f0e3af7f15e4f0516\josephineoe.github.io-8a4babfcf759926128ab721f0e3af7f15e4f0516\assets\images\projects\pov\Team 3-Report.pdf"
rviz_path = r"C:\Users\JosephineOE\Downloads\josephineoe.github.io-8a4babfcf759926128ab721f0e3af7f15e4f0516\josephineoe.github.io-8a4babfcf759926128ab721f0e3af7f15e4f0516\assets\images\projects\rviz_maze\Applications of ROS_Exploring Autonomous Navigat.pdf"

def extract_pdf_content(pdf_path, name):
    """Extract full text content from PDF"""
    print(f"\n{'='*80}")
    print(f"{name} PDF EXTRACTION")
    print(f"{'='*80}\n")
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"Total pages: {len(pdf.pages)}\n")
            full_text = ""
            
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    full_text += f"\n--- PAGE {i+1} ---\n{text}\n"
            
            # Save to file for review
            output_file = f"{name.lower().replace('/', '_')}_content.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(full_text)
            
            print(f"Content saved to {output_file}")
            print(f"Total characters extracted: {len(full_text)}")
            
            # Print first 2000 characters
            print("\nFirst 2000 characters:")
            print(full_text[:2000])
            print("\n...")
            
            return full_text
    except Exception as e:
        print(f"Error extracting {name}: {e}")
        return None

# Extract both PDFs
pov_content = extract_pdf_content(pov_path, "POV")
rviz_content = extract_pdf_content(rviz_path, "ROS/RViz Maze")
