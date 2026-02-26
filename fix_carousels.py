import re

def update_file(filename, replacement_track, role_content=None, team_content=None):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace carousel track
    pattern = r'(<div class="case-carousel__track">)(.*?)(</div>\s*<button class="case-carousel__btn case-carousel__btn--prev")'
    new_content = re.sub(pattern, r'\1\n' + replacement_track + r'\n                    \3', content, flags=re.DOTALL)
    
    # Replace role content if provided
    if role_content:
        role_pattern = r'(<h3 class="role-team__heading">My Role</h3>\s*<p class="role-team__description">).*?(</p>)'
        new_content = re.sub(role_pattern, r'\g<1>' + role_content + r'\2', new_content, flags=re.DOTALL)
        
    # Replace team content if provided
    if team_content:
        team_pattern = r'(<h3 class="role-team__heading">My Team</h3>\s*)(<p class="role-team__description">.*?</p>|<div class="role-team__list">.*?</div>)'
        
        team_html = '<div class="role-team__list">\n'
        for member in team_content:
            team_html += f'                        <span class="role-team__member">{member}</span>\n'
        team_html += '                    </div>'
        
        new_content = re.sub(team_pattern, r'\g<1>' + team_html, new_content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

homes_carousel = """                        <!-- 1. Research and discovery -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">1. Research and discovery</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);">Research about the real estate industry to better understand the concept of fractional ownership.</li>
                                    <li style="margin-bottom: var(--space-sm);">Multiple stakeholder interviews with the Homes Collection team to refine our understanding of their core requirements.</li>
                                    <li>Competitor analysis to understand differentiations, USPs, processes that gave a view of the positioning of Homes Collection in the industry.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 2. Product documentation -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">2. Product documentation</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);">Compiling the research into data points to plan different user journeys for users to achieve their goal.</li>
                                    <li>Documenting all journeys in a PRD (Product requirement documentation) that helps us keep everyone on the same track about the product.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 3. Mid-fidelity design -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">3. Mid-fidelity design</h3>
                                <p class="case-carousel__slide-text" style="text-align: left;">Structuring all the documented data into web pages, ensuring accessibility through placements of the information at right place which helps the user achieve their goals at different touch points</p>
                            </div>
                        </div>

                        <!-- 4. Design system -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">4. Design system</h3>
                                <p class="case-carousel__slide-text" style="text-align: left;">Created the foundation of the design language to scale across web designs with uniformity and consistency. Created the design elements and converting them into components to facilitate effective work processes</p>
                            </div>
                        </div>

                        <!-- 5. High-fidelity design -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">5. High-fidelity design</h3>
                                <p class="case-carousel__slide-text" style="text-align: left;">Created high-fidelity design screens to enhance communication visually and elevate the brand's understanding using retentive brand elements. We also implemented a unique visual direction to bring in the premium look and feel of the business to create an aspirational value for the potential users of the properties.</p>
                            </div>
                        </div>

                        <!-- 6. Development -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">6. Development</h3>
                                <p class="case-carousel__slide-text" style="text-align: left; margin-bottom: var(--space-sm);">The challenges of building a user facing product and an admin dashboard for Homes Collection was to:</p>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);">Integrate third party event management tool in our system, to keep a track of entire buying process from initiating user interest till getting the share transfer certificate</li>
                                    <li style="margin-bottom: var(--space-sm);">Integrating the third party tool to experience a property virtually</li>
                                    <li style="margin-bottom: var(--space-sm);">Our team analysed the above business requirements and the importance of the above features to enhance the users’ experience on the Homes collection platform. We converted the business requirements into the a user facing product and also created an admin dashboard for the client to seamlessly manage users’ data to help the business development needs.</li>
                                    <li>The product requirement document is of major importance at this stage in bringing the client requirements and the development feasibilities in check.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 7. QA and testing -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">7. QA and testing</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);">Conduct end-to-end system testing to validate the overall functionality of the Homes Collection platform.</li>
                                    <li style="margin-bottom: var(--space-sm);">Test the admin dashboard to ensure seamless management of user data</li>
                                    <li style="margin-bottom: var(--space-sm);">Verify each functional component individually according to the high-fidelity design and PRD.</li>
                                    <li style="margin-bottom: var(--space-sm);">Test the different touchpoints to ensure users can achieve their goals effectively.</li>
                                    <li style="margin-bottom: var(--space-sm);">Validate the implementation of the design system to ensure uniformity and consistency.</li>
                                    <li>Test the responsiveness and loading times of web pages to guarantee a smooth user experience.</li>
                                </ul>
                            </div>
                        </div>"""

gray_carousel = """                        <!-- 1. Research and Discovery -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">1. Research and Discovery</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);">Engage key stakeholders to understand their experiences with the current LMS and expectations for the new one.</li>
                                    <li style="margin-bottom: var(--space-sm);">Identify the specific needs and preferences of movement professionals and individuals engaging with Gray Institute® courses.</li>
                                    <li style="margin-bottom: var(--space-sm);">Assess the effectiveness of various content formats offered, considering user preferences and feedback.</li>
                                    <li style="margin-bottom: var(--space-sm);">Analyze user adoption patterns and feedback for the new LMS (GIFT) to understand user experiences and satisfaction.</li>
                                    <li style="margin-bottom: var(--space-sm);">Research other platforms, identifying best practices, features, and potential gaps for Gray Institute®.</li>
                                    <li>Map out the user journey, identifying pain points and opportunities for a smoother learning experience.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 2. Product Documentation -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">2. Product Documentation</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);">Collaborate with the client to define the overall goals and objectives for the new LMS.</li>
                                    <li style="margin-bottom: var(--space-sm);">Create detailed user personas to represent the target audience, their motivations, and pain points.</li>
                                    <li style="margin-bottom: var(--space-sm);">Define functional and non-functional requirements for the LMS, including features like course management, user registration, and assessment tools.</li>
                                    <li style="margin-bottom: var(--space-sm);">Design a clear and intuitive information architecture to organize courses, modules, and other learning materials.</li>
                                    <li>Develop a comprehensive product roadmap, outlining key milestones and timelines for development.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 3. Mid-fidelity Design -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">3. Mid-fidelity Design</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);">Building low-fidelity wireframes to visualize the core layout and user flow of the LMS.</li>
                                    <li style="margin-bottom: var(--space-sm);">Developing high-fidelity wireframes to incorporate more detailed design elements and Interactions.</li>
                                    <li style="margin-bottom: var(--space-sm);">Creating interactive prototypes to test the usability and flow of the LMS with potential users and stakeholders.</li>
                                    <li style="margin-bottom: var(--space-sm);">Conducting usability testing with movement professionals and individuals to identify areas for improvement.</li>
                                    <li>Refining the design based on user feedback and testing results to ensure a seamless learning experience.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 4. Design System -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">4. Design System</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);">Establish a consistent visual identity for the LMS, including typography, color palette, and iconography.</li>
                                    <li style="margin-bottom: var(--space-sm);">Develop a library of reusable UI components to ensure uniformity across the platform.</li>
                                    <li style="margin-bottom: var(--space-sm);">Define a clear set of design principles and guidelines to maintain consistency and quality.</li>
                                    <li style="margin-bottom: var(--space-sm);">Design an icon set that is intuitive and easy to understand for users.</li>
                                    <li>Create a comprehensive style guide that outlines all design elements and their usage.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 5. High-fidelity Design -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">5. High-fidelity Design</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);">Refine the design language by incorporating brand elements and creating a visually appealing and engaging interface.</li>
                                    <li style="margin-bottom: var(--space-sm);">Design individual course pages, including layouts for video content, text, quizzes, and other learning materials.</li>
                                    <li style="margin-bottom: var(--space-sm);">Design high-fidelity screens for all LMS features, ensuring a consistent look and feel across the platform.</li>
                                    <li style="margin-bottom: var(--space-sm);">Create more complex interactive prototypes to simulate the complete learning experience and gather further user feedback.</li>
                                    <li>Finalize the design for all screens and interactions, ensuring they meet the defined requirements and user needs.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 6. Development -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">6. Development</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);">Develop the LMS based on the finalized design and requirements, ensuring scalability and performance.</li>
                                    <li style="margin-bottom: var(--space-sm);">Build the frontend and backend of the platform, incorporating all features and functionalities.</li>
                                    <li style="margin-bottom: var(--space-sm);">Integrate the LMS with any necessary third-party tools or systems, such as payment gateways or email services.</li>
                                    <li style="margin-bottom: var(--space-sm);">Optimize the platform for mobile devices to provide a seamless learning experience across different screen sizes.</li>
                                    <li>Implement security measures to protect user data and ensure the privacy of learning materials.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 7. QA and Testing -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">7. QA and Testing</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);">Conduct thorough testing to identify and fix any bugs or issues across different browsers and devices.</li>
                                    <li style="margin-bottom: var(--space-sm);">Perform end-to-end testing to ensure all features and functionalities are working as expected.</li>
                                    <li style="margin-bottom: var(--space-sm);">Gather feedback from movement professionals and individuals during beta testing to further refine the platform.</li>
                                    <li style="margin-bottom: var(--space-sm);">Test the LMS for security and data privacy to ensure the safety of user information and learning materials.</li>
                                    <li>Validate the platform's performance and scalability under various user loads.</li>
                                </ul>
                            </div>
                        </div>"""

milestone_carousel = """                        <!-- 1. Discovery and Planning -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">1. Discovery and Planning</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);">Identified challenges and concerns from Milestone founders.</li>
                                    <li style="margin-bottom: var(--space-sm);">Defined project objectives and requirements.</li>
                                    <li style="margin-bottom: var(--space-sm);">Explored key parameters for success, considering user behaviors of both children and parents.</li>
                                    <li style="margin-bottom: var(--space-sm);">Conceptualized the components of the app based on the identified user behaviors.</li>
                                    <li>Formulated hypotheses for the key functionality of the app.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 2. Product Documentation -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">2. Product Documentation</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);">Clearly outlined the vision and goals of Milestone – a financial literacy app for children.</li>
                                    <li style="margin-bottom: var(--space-sm);">Defined the target audience, focusing on parents and kids in the APAC region.</li>
                                    <li style="margin-bottom: var(--space-sm);"><strong>Feature Specification:</strong> Detailed the essential features, including guided onboarding, collaborative goal setting, positive reinforcement through chores, bite-sized learning quests, and gamified milestones. Documented the inclusion of an inclusive 'Guardians' concept, allowances, interest, and other key functionalities.</li>
                                    <li><strong>Requirements Analysis:</strong> Conducted thorough analysis to identify technical and user requirements. Documented functionalities necessary for seamless user experience and efficient app management.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 3. Mid-fidelity Design -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">3. Mid-fidelity Design</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);"><strong>Wireframing:</strong> Developed mid-fidelity wireframes outlining the app's basic structure, layout, and functionality. Ensured wireframes reflected collaborative goal setting, positive reinforcement, and other essential features.</li>
                                    <li><strong>Prototyping:</strong> Constructed interactive prototypes using tools like Figma to simulate user journeys. Validated hypotheses and gathered feedback from stakeholders and potential users.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 4. Design System -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">4. Design System</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);"><strong>Visual Identity:</strong> Collaborated with vendors to establish the visual identity for Milestone. Incorporated branding elements into UI designs, ensuring alignment with the brand's values.</li>
                                    <li><strong>Design Components:</strong> Developed a set of design components and patterns for consistent use across the app. Ensured a cohesive design language for both the parent and child-facing mobile apps.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 5. High-fidelity Design -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">5. High-fidelity Design</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);"><strong>Detailed UI Design:</strong> Enhanced wireframes into high-fidelity designs with detailed visual elements. Ensured the designs maintained a balance between aesthetics and usability.</li>
                                    <li><strong>User Feedback Iterations:</strong> Incorporated feedback from stakeholders and user testing into the high-fidelity design. Made necessary adjustments to enhance the overall user experience.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 6. Development -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">6. Development</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);"><strong>Frontend and Backend Development:</strong> Collaborated with development teams to implement the designed features. Ensured alignment with the established design system and maintained design integrity.</li>
                                    <li><strong>CI/CD Implementation:</strong> Set up Continuous Integration/Continuous Deployment pipelines for efficient development and deployment processes. Monitored progress to ensure timely delivery of features.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 7. QA and Testing -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">7. QA and Testing</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);"><strong>Testing Strategy:</strong> Developed a comprehensive testing strategy covering test cases and scenarios for each functionality.</li>
                                    <li><strong>User Acceptance Testing (UAT):</strong> Engaged stakeholders and potential users in UAT to validate the app's usability and functionality. Addressed identified issues promptly and iteratively improved the app.</li>
                                </ul>
                            </div>
                        </div>"""

asvi_carousel = """                        <!-- 1. Branding - Onboarding questionnaires -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">1. Branding - Onboarding questionnaires</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li>Developed detailed onboarding questionnaires to delve into the nuances of ASVI Thoughtworks. Explored aspects such as business objectives, website requirements, tone of voice, brand personality, core brand fundamentals, target audience, and a thorough understanding of competitors and third-party tools.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 2. Branding - Service design architecture -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">2. Branding - Service design architecture</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);">Conceptualized and designed a service design architecture that outlined the workflow and services provided by ASVI Thoughtworks and its clients.</li>
                                    <li style="margin-bottom: var(--space-sm);"><strong>Problems:</strong> Mapped out tools, frameworks, and processes to address identified problems.</li>
                                    <li style="margin-bottom: var(--space-sm);"><strong>Deliverables:</strong> Specified tangible outcomes and outputs expected from the project.</li>
                                    <li style="margin-bottom: var(--space-sm);"><strong>Impact of Problem-Solving:</strong> Explored the potential impact of addressing identified issues.</li>
                                    <li><strong>Offerings and Services:</strong> Defined the range of services ASVI Thoughtworks would provide through the platform.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 3. Branding - Secondary research -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">3. Branding - Secondary research</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li>Conducted thorough secondary research to analyze competitors in the HR solutions space. Evaluated their strengths and weaknesses, allowing us to refine our own strategy and design based on industry best practices. Integrated findings into the service design architecture to ensure differentiation and innovation.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 4. Branding - Brand visual identity design -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">4. Branding - Brand visual identity design</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);"><strong>Development of Cohesive Visual Identity:</strong></li>
                                    <li>Translated the brand personality and fundamentals into a cohesive visual identity. Created a distinctive logo, color palette, typography, and other design elements that represented ASVI Thoughtworks' values and objectives.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 5. Branding - Website design on webflow -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">5. Branding - Website design on webflow</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);"><strong>Execution of Web Design:</strong></li>
                                    <li>Translated the brand visual identity into the design of the ASVI Thoughtworks website using Webflow. Ensured a user-friendly and visually appealing interface that reflected the brand's professionalism and commitment to innovation.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 6. Product Design - Goal definition of stakeholder -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">6. Product Design - Goal definition of stakeholder</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);"><strong>Utilizing Service Design Architecture</strong></li>
                                    <li>Leveraged the previously defined service design architecture to set clear and achievable goals for each stakeholder involved in the HR platform. Documented these goals to serve as a guide for the subsequent design phases.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 7. Product Design - Mid-fidelity design -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">7. Product Design - Mid-fidelity design</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);"><strong>Development of Mid-Fidelity Wireframes and User Flows:</strong> Created mid-fidelity wireframes and mapped out the user journey for each stakeholder. Developed wireframes and user flows to visually represent the interaction and navigation within the platform.</li>
                                    <li><strong>Stakeholder Testing and Feedback:</strong> Conducted testing with relevant stakeholders to gather valuable feedback on the mid-fidelity design. Incorporated suggestions and refinements to ensure the final product aligns with user expectations and needs.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- 8. Product Design - High-fidelity design -->
                        <div class="case-carousel__slide">
                            <div class="case-carousel__slide-content" style="text-align: left;">
                                <h3 class="case-carousel__title" style="text-align: left; border-bottom: 1px solid var(--border-subtle); padding-bottom: var(--space-sm); margin-bottom: var(--space-md);">8. Product Design - High-fidelity design</h3>
                                <ul style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);">
                                    <li style="margin-bottom: var(--space-sm);"><strong>Cohesive Brand Integration:</strong></li>
                                    <li>Infused brand identity elements into the mid-fidelity design to maintain consistency with the established visual identity. Ensured that the user experience aligns seamlessly with the overall brand image. Awaiting client approval before moving on to the development phase.</li>
                                </ul>
                            </div>
                        </div>"""

update_file("case-studies/homes-collection.html", homes_carousel)

milestone_role = "In the Milestone project, I played a dual role. I collaborated with the team to design user-friendly interfaces for both parent and child-facing mobile apps. Simultaneously, I took charge of designing and managing the admin dashboard. This dual responsibility allowed me to contribute to the comprehensive design strategy, ensuring a seamless experience for both end-users and administrators in line with Milestone's objectives."
milestone_team = [
    "Vaibhav Amin - UX UI Designer",
    "Nidhi - UX UI Designer",
    "Kuldeep - UX UI Designer",
    "Nayan - Frontend Developer",
    "Saloni - Frontend Developer",
    "Jatin - Mobile App Developer",
    "Nikhil - Mobile App Developer",
    "Sanket - Mobile App Developer",
    "Siddheshwar - Backend Developer",
    "Mujahid - QA Lead"
]
update_file("case-studies/milestone.html", milestone_carousel, role_content=milestone_role, team_content=milestone_team)

asvi_role = "This case study emphasizes my integral role as a collaborator in the branding phase and leader in the product design phase of the ASVI Thoughtworks project. By understanding business intricacies, conducting thorough research, and ensuring brand consistency in the design process, I contributed to a solution that not only met but exceeded the expectations of ASVI Thoughtworks and its clients."
asvi_team = [
    "Vaibhav Amin - UX UI Designer",
    "Nidhi - UX UI Designer",
    "Sonia - UX UI Designer",
    "Saurabh - Graphic Designer",
    "Kunika - Content Strategist",
    "Jaykrishna - Frontend Developer"
]
update_file("case-studies/asvi-thoughtworks.html", asvi_carousel, role_content=asvi_role, team_content=asvi_team)

update_file("case-studies/gray-institute.html", gray_carousel)

print("Updates applied successfully.")
