---
layout: default
published: true
title: Contact
permalink: /contact/
---

<div class="hero-section" style="padding: 100px 0; background: var(--background-color); border-bottom: 1px solid var(--border-color); text-align: center;">
	<div class="container">
		<h1 style="font-size: var(--font-size-3xl); letter-spacing: -0.02em; color: var(--text-primary);">Get In Touch</h1>
		<p style="color: var(--text-secondary); opacity: 0.7; max-width: 600px; margin: 0 auto; font-weight: 300;">Have a question, collaboration idea, or want to discuss robotics and AI projects? I'd love to hear from you.</p>
	</div>
</div>

<div class="contact-section">
	<div class="container">
		<div class="contact-wrapper">
			<!-- Contact Form -->
			<div class="contact-form-wrapper">
				<h2>Send a Message</h2>
				<form action="https://formspree.io/f/xyzqwpby" method="POST" class="contact-form">
					<div class="form-group">
						<label for="name" class="form-label">Name</label>
						<input 
							type="text" 
							id="name" 
							name="name" 
							required
							placeholder="Your name"
							class="form-input"
						>
					</div>

					<div class="form-group">
						<label for="email" class="form-label">Email</label>
						<input 
							type="email" 
							id="email" 
							name="email" 
							required
							placeholder="your.email@example.com"
							class="form-input"
						>
					</div>

					<div class="form-group">
						<label for="subject" class="form-label">Subject</label>
						<input 
							type="text" 
							id="subject" 
							name="subject" 
							placeholder="What is this about?"
							class="form-input"
						>
					</div>

					<div class="form-group">
						<label for="message" class="form-label">Message</label>
						<textarea 
							id="message" 
							name="message" 
							rows="8" 
							required
							placeholder="Tell me more about your inquiry..."
							class="form-textarea"
						></textarea>
					</div>

					<button type="submit" class="btn-submit">Send Message</button>
					<p class="form-note">Powered by <a href="https://formspree.io/" target="_blank" rel="noopener noreferrer">Formspree</a> · No spam, ever.</p>
				</form>
			</div>

			<!-- Contact Information -->
			<div class="contact-info-wrapper">
				<h2>Connect With Me</h2>
				<p class="contact-intro">I'm passionate about robotics, embodied AI, assistive technology, and exploring how technology can create meaningful impact. Whether you have a collaboration opportunity, questions about my work, or just want to connect—I'd be happy to hear from you.</p>

				<div class="contact-methods">
					<div class="contact-method">

						<h3>💼 LinkedIn</h3>
						<p>Connect and follow my professional journey</p>
						<a href="https://www.linkedin.com/in/josephineodusanya/" target="_blank" rel="noopener noreferrer" class="contact-link">Visit LinkedIn</a>
					</div>

					<div class="contact-method">
						<h3>🐙 GitHub</h3>
						<p>Explore my open-source projects and code</p>
						<a href="https://github.com/josephineoe" target="_blank" rel="noopener noreferrer" class="contact-link">Visit GitHub</a>
					</div>

					<div class="contact-method">
						<h3>📱 Social</h3>
						<p>Follow me on social media</p>
						<div class="social-links">
							<a href="https://twitter.com/[PLACEHOLDER: Twitter Handle]" target="_blank" rel="noopener noreferrer" class="social-link">Twitter</a>
							<a href="https://instagram.com/[PLACEHOLDER: Instagram Handle]" target="_blank" rel="noopener noreferrer" class="social-link">Instagram</a>
						</div>
					</div>
				</div>

				<div class="availability-note">
					<p><strong>Response Time:</strong> I typically respond to messages within [PLACEHOLDER: 1-2 business days]. Thank you for reaching out!</p>
				</div>
			</div>
		</div>
	</div>
</div>

<style>
.contact-section {
	padding: 60px 0;
	background: var(--background-color);
}

.contact-wrapper {
	display: grid;
	grid-template-columns: 1fr 1fr;
	gap: var(--spacing-2xl);
	align-items: start;
}

.contact-form-wrapper {
	background-color: var(--surface-color);
	padding: var(--spacing-2xl);
	border-radius: var(--radius-lg);
	border: 1px solid var(--border-color);
}

.contact-form-wrapper h2 {
	color: var(--text-primary);
	margin-bottom: var(--spacing-lg);
	margin-top: 0;
}

.contact-form {
	display: flex;
	flex-direction: column;
	gap: var(--spacing-lg);
}

.form-group {
	display: flex;
	flex-direction: column;
	gap: var(--spacing-xs);
}

.form-label {
	color: var(--text-primary);
	font-weight: var(--font-weight-medium);
	font-size: var(--font-size-sm);
}

.form-input,
.form-textarea {
	padding: 12px 16px;
	border: 1px solid var(--border-color);
	border-radius: var(--radius-md);
	background-color: var(--background-color);
	color: var(--text-primary);
	font-family: inherit;
	font-size: var(--font-size-base);
	transition: all 0.3s ease;
}

.form-input::placeholder,
.form-textarea::placeholder {
	color: var(--text-secondary);
	opacity: 0.6;
}

.form-input:focus,
.form-textarea:focus {
	outline: none;
	border-color: var(--primary-color);
	box-shadow: 0 0 0 3px rgba(var(--primary-color-rgb), 0.1);
	background-color: var(--surface-color);
}

.form-textarea {
	resize: vertical;
	min-height: 200px;
	font-family: monospace;
}

.btn-submit {
	padding: 14px 28px;
	background-color: var(--primary-color);
	color: white;
	border: none;
	border-radius: var(--radius-md);
	font-weight: var(--font-weight-medium);
	font-size: var(--font-size-base);
	cursor: pointer;
	transition: all 0.3s ease;
	align-self: flex-start;
	margin-top: var(--spacing-md);
}

.btn-submit:hover {
	background-color: var(--primary-color-dark);
	transform: translateY(-2px);
	box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.btn-submit:active {
	transform: translateY(0);
}

.form-note {
	color: var(--text-secondary);
	font-size: var(--font-size-xs);
	margin-top: var(--spacing-md);
	margin-bottom: 0;
}

.form-note a {
	color: var(--primary-color);
	text-decoration: none;
}

.form-note a:hover {
	text-decoration: underline;
}

.contact-info-wrapper {
	display: flex;
	flex-direction: column;
	gap: var(--spacing-lg);
}

.contact-info-wrapper h2 {
	color: var(--text-primary);
	margin-top: 0;
	margin-bottom: var(--spacing-md);
}

.contact-intro {
	color: var(--text-secondary);
	line-height: 1.6;
	margin-bottom: var(--spacing-lg);
}

.contact-methods {
	display: flex;
	flex-direction: column;
	gap: var(--spacing-lg);
	margin-bottom: var(--spacing-xl);
}

.contact-method {
	padding: var(--spacing-lg);
	background-color: var(--surface-color);
	border-radius: var(--radius-md);
	border: 1px solid var(--border-color);
	transition: all 0.3s ease;
}

.contact-method:hover {
	border-color: var(--primary-color);
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.contact-method h3 {
	color: var(--text-primary);
	margin-top: 0;
	margin-bottom: var(--spacing-xs);
	font-size: var(--font-size-base);
}

.contact-method p {
	color: var(--text-secondary);
	font-size: var(--font-size-sm);
	margin: var(--spacing-xs) 0;
}

.contact-link {
	display: inline-block;
	color: var(--primary-color);
	text-decoration: none;
	font-weight: var(--font-weight-medium);
	margin-top: var(--spacing-sm);
	padding: 8px 12px;
	border-radius: var(--radius-md);
	transition: all 0.3s ease;
	border: 1px solid transparent;
}

.contact-link:hover {
	background-color: rgba(var(--primary-color-rgb), 0.1);
	border-color: var(--primary-color);
}

.social-links {
	display: flex;
	gap: var(--spacing-md);
	margin-top: var(--spacing-sm);
}

.social-link {
	color: var(--primary-color);
	text-decoration: none;
	font-size: var(--font-size-sm);
	padding: 6px 12px;
	border: 1px solid var(--border-color);
	border-radius: var(--radius-md);
	transition: all 0.3s ease;
}

.social-link:hover {
	background-color: var(--primary-color);
	color: white;
	border-color: var(--primary-color);
}

.availability-note {
	padding: var(--spacing-lg);
	background-color: rgba(var(--primary-color-rgb), 0.05);
	border-left: 4px solid var(--primary-color);
	border-radius: var(--radius-md);
	color: var(--text-secondary);
	font-size: var(--font-size-sm);
	margin-top: var(--spacing-lg);
}

.availability-note p {
	margin: 0;
}

/* Responsive Design */
@media (max-width: 968px) {
	.contact-wrapper {
		grid-template-columns: 1fr;
		gap: var(--spacing-lg);
	}

	.contact-form-wrapper,
	.contact-info-wrapper {
		width: 100%;
	}
}

@media (max-width: 640px) {
	.contact-section {
		padding: 40px 0;
	}

	.contact-form-wrapper {
		padding: var(--spacing-lg);
	}

	.form-input,
	.form-textarea {
		padding: 10px 12px;
		font-size: 16px;
	}

	.btn-submit {
		width: 100%;
		align-self: stretch;
	}

	.social-links {
		flex-wrap: wrap;
	}
}

/* FORM SUCCESS STYLES */
.formspree-success {
	background-color: #d4edda;
	border: 1px solid #c3e6cb;
	color: #155724;
	padding: var(--spacing-lg);
	border-radius: var(--radius-md);
	margin-bottom: var(--spacing-lg);
}

.formspree-error {
	background-color: #f8d7da;
	border: 1px solid #f5c6cb;
	color: #721c24;
	padding: var(--spacing-lg);
	border-radius: var(--radius-md);
	margin-bottom: var(--spacing-lg);
}
</style>
