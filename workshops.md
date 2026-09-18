---
layout: default
published: true
title: Workshops
permalink: /workshops/
---

<div class="hero-section" style="padding: 100px 0; background: var(--background-color); border-bottom: 1px solid var(--border-color); text-align: center;">
	<div class="container">
		<h1 style="font-size: var(--font-size-3xl); letter-spacing: -0.02em; color: var(--text-primary);">Workshops</h1>
		<p style="color: var(--text-secondary); opacity: 0.7; max-width: 600px; margin: 0 auto; font-weight: 300;">I host hands-on workshops on robotics, mechatronics, and embodied AI for classrooms, student orgs, and companies looking to make engineering approachable and fun.</p>
	</div>
</div>

<div class="workshops-section">
	<div class="container">

		<div class="workshops-intro">
			<h2>What I Offer</h2>
			<p class="workshops-intro-text">
				Whether you're introducing students to robotics for the first time or want a hands-on session for your team, I design and lead workshops that mix approachable theory with real, hands-on building. Sessions can be tailored in length, depth, and topic to fit your audience—from a one-hour intro to a multi-day build sprint.
			</p>
		</div>

		<div class="workshops-grid">
			<div class="workshop-card">
				<div class="workshop-card-icon">🤖</div>
				<h3>Intro to Robotics</h3>
				<p>Beginner-friendly sessions covering sensors, actuators, and control—great for students getting their first hands-on experience with hardware.</p>
			</div>

			<div class="workshop-card">
				<div class="workshop-card-icon">🛠️</div>
				<h3>Mechatronics & Prototyping</h3>
				<p>Bridging mechanical design, electronics, and code through guided build sessions using Arduino, 3D printing, and CAD.</p>
			</div>

			<div class="workshop-card">
				<div class="workshop-card-icon">🧠</div>
				<h3>Embodied AI & Assistive Tech</h3>
				<p>A look at how AI and robotics come together to build assistive systems, with discussion-driven and project-based formats.</p>
			</div>

			<div class="workshop-card">
				<div class="workshop-card-icon">✨</div>
				<h3>Custom Sessions</h3>
				<p>Have something specific in mind? I work with organizers to design a workshop around your group's goals, skill level, and time constraints.</p>
			</div>
		</div>

		<div class="workshops-events">
			<div class="workshops-events-column">
				<h2>Upcoming Events</h2>
				<div class="workshops-events-placeholder">
					<p>No upcoming workshops scheduled right now—check back soon!</p>
				</div>
			</div>

			<div class="workshops-events-column">
				<h2>Past Events</h2>
				<div class="workshops-events-placeholder">
					<p>Past workshop recaps and links will be added here soon.</p>
				</div>
			</div>
		</div>

		<div class="workshops-cta">
			<h2>Book a Workshop</h2>
			<p>Interested in hosting a workshop for your school, club, or company? I'd love to hear about your group and what you're hoping to learn.</p>
			<a href="{{ '/contact/' | relative_url }}" class="workshops-cta-link">Get In Touch</a>
		</div>

	</div>
</div>

<style>
.workshops-section {
	padding: 60px 0;
	background: var(--background-color);
}

.workshops-intro {
	max-width: 760px;
	margin: 0 auto var(--spacing-2xl);
	text-align: center;
}

.workshops-intro h2 {
	color: var(--text-primary);
	margin-top: 0;
}

.workshops-intro-text {
	color: var(--text-secondary);
	line-height: 1.6;
}

.workshops-grid {
	display: grid;
	grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
	gap: var(--spacing-lg);
	margin-bottom: var(--spacing-2xl);
}

.workshop-card {
	padding: var(--spacing-lg);
	background-color: var(--surface-color);
	border: 1px solid var(--border-color);
	border-radius: var(--radius-lg);
	transition: all 0.3s ease;
}

.workshop-card:hover {
	border-color: var(--primary-color);
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
	transform: translateY(-2px);
}

.workshop-card-icon {
	font-size: var(--font-size-2xl);
	margin-bottom: var(--spacing-sm);
}

.workshop-card h3 {
	color: var(--text-primary);
	margin: 0 0 var(--spacing-xs);
	font-size: var(--font-size-base);
}

.workshop-card p {
	color: var(--text-secondary);
	font-size: var(--font-size-sm);
	line-height: 1.6;
	margin: 0;
}

.workshops-events {
	display: grid;
	grid-template-columns: 1fr 1fr;
	gap: var(--spacing-2xl);
	margin-bottom: var(--spacing-2xl);
	padding-top: var(--spacing-2xl);
	border-top: 1px solid var(--border-color);
}

.workshops-events-column h2 {
	color: var(--text-primary);
	margin-top: 0;
	margin-bottom: var(--spacing-md);
}

.workshops-events-placeholder {
	padding: var(--spacing-lg);
	background-color: var(--surface-color);
	border: 1px dashed var(--border-color);
	border-radius: var(--radius-md);
}

.workshops-events-placeholder p {
	color: var(--text-secondary);
	font-size: var(--font-size-sm);
	margin: 0;
}

.workshops-cta {
	text-align: center;
	padding: var(--spacing-2xl);
	background-color: rgba(var(--primary-color-rgb), 0.05);
	border-radius: var(--radius-lg);
}

.workshops-cta h2 {
	color: var(--text-primary);
	margin-top: 0;
}

.workshops-cta p {
	color: var(--text-secondary);
	max-width: 500px;
	margin: 0 auto var(--spacing-lg);
	line-height: 1.6;
}

.workshops-cta-link {
	display: inline-block;
	padding: 12px 28px;
	background-color: var(--primary-color);
	color: white;
	text-decoration: none;
	border-radius: var(--radius-md);
	font-weight: var(--font-weight-medium);
	transition: all 0.3s ease;
}

.workshops-cta-link:hover {
	background-color: var(--primary-color-dark);
	transform: translateY(-2px);
	box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Responsive Design */
@media (max-width: 768px) {
	.workshops-events {
		grid-template-columns: 1fr;
		gap: var(--spacing-lg);
	}
}

@media (max-width: 640px) {
	.workshops-section {
		padding: 40px 0;
	}

	.workshops-cta {
		padding: var(--spacing-lg);
	}
}
</style>
