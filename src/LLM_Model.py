import json
import requests
from bs4 import BeautifulSoup
from . import CTAs_SubCTAs


class LLM_Model:
    max_webscraper_text_length = 2048

    categorization_prmopt = """
You are tasked with categorizing a company based on its information.
Use the company's objective as the most important criteria for categorization.
Focus on the core business and the overall domain of the company as described.
Do **not** categorize it based off secondary information such as how the product is powered.

Here a list of "sub CTAs" and their descriptions:

"Human Performance Enhancement": Biotechnologies improving soldiers’ physical, cognitive, and health performance through genomics, drugs, and augmentation tools.
"Regenerative Medicine": Creating bioengineered tissues, organs, and advanced prosthetics to treat battlefield injuries and restore functionality.
"Neurotechnology & Brain-Computer Interfaces": Integrating neural systems with technology for cognitive enhancement, neuroprosthetics, and direct brain-machine communication.
"5G & Beyond Networks": Ultra-fast, secure, low-latency communication with edge computing and network slicing for real-time, mission-critical military operations.
"mmWave Technology": High-bandwidth, secure, short-range communications ideal for drones, vehicles, and soldiers in dense, contested environments.
"Massive MIMO": Improves signal strength and transmission rates using large antenna arrays, enabling reliable communication in complex battlefield conditions.
"Mesh Networking": Dynamic, decentralized networks providing resilient communication in the field without reliance on central infrastructure.
"Spectrum Sharing & Cognitive Radio": Adaptive access to available frequencies and interference avoidance for uninterrupted communication in congested, contested environments.
"THz Technology": Ultra-fast data transmission and high-resolution sensing through materials, enabling advanced imaging and secure communication.
"Nanomaterials": Ultra-light, strong materials for enhanced armor, coatings with anti-corrosion and self-healing properties for military vehicles and equipment.
"Metamaterials": Engineered for stealth and cloaking technologies by manipulating electromagnetic waves, enabling radar and infrared invisibility.
"Smart Materials": Self-healing polymers and shape-memory alloys for adaptive military platforms and structures with reduced maintenance needs.
"Advanced Ceramics & Composites": High-temperature, high-strength materials for ballistic protection, jet engines, and hypersonic vehicles.
"Graphene & 2D Materials": Lightweight, flexible materials for energy storage, sensors, and military electronics with superior durability.
"High-Entropy Alloys": Multi-element alloys with extreme strength, corrosion resistance, and wear-resistant coatings for operations in harsh environments.
"Explainable AI (XAI)": AI systems that provide transparent, understandable decision-making, fostering trust and effective human-AI collaboration in military operations.
"Autonomous Unmanned Vehicles & Systems": Unmanned aerial, ground, and underwater systems conducting reconnaissance, logistics, and combat missions with minimal human intervention.
"Swarm Intelligence": Groups of autonomous systems collaborating to perform tasks like surveillance, reconnaissance, and coordinated strikes through distributed sensing and communication.
"Cyber Defense AI": AI-driven systems detecting and mitigating cyber threats, automating responses to protect military networks and critical infrastructure.
"Autonomous Weapons Systems": AI-enhanced systems capable of identifying, targeting, and engaging threats autonomously, including lethal and defensive autonomous weapons.
"Command & Control AI": AI systems providing real-time battlefield insights, optimizing decision-making, mission coordination, and logistics in complex environments.
"Multi-Domain Command and Control (MDC2)": Enables real-time, cross-domain communication and coordination, optimizing decision-making across air, land, sea, space, and cyber operations.
"Interoperability Standards and Protocols": Ensures diverse systems work together via standardized communication protocols and open architectures for seamless data exchange.
"Tactical Edge Networking": Provides secure, low-latency communication for soldiers in remote areas using resilient, decentralized networks like mobile ad hoc networks (MANETs).
"Cyber-Physical Systems (CPS)": Integrates sensors, autonomous platforms, and physical systems for real-time responsiveness and cyber protection in defense applications.
"Joint All-Domain Command and Control (JADC2)": Real-time data fusion and AI-driven automation for unified information sharing across military services and operational domains.
"Resilient Network Architectures": Self-healing, mesh, and hybrid networks designed to ensure secure, reliable communication in contested environments.
"Edge Computing and Distributed Systems": Processes data at the source using edge devices, reducing latency and enabling real-time AI-powered decision-making in the field.
"Radiation-Hardened Electronics": Electronics designed to withstand radiation in space and nuclear environments, ensuring reliable functionality for satellites and military systems in extreme conditions.
"Trusted Microelectronics": Secure, tamper-resistant microchips ensuring supply chain integrity and preventing hardware-based cyber threats in critical military systems.
"Chip-Scale Atomic Clocks (CSACs)": Ultra-precise, low-power timing devices for secure communications and navigation in GPS-denied environments.
"Advanced Packaging & Integration": 3D-integrated circuits and system-in-package technologies improving performance, size, weight, and power efficiency for military electronics.
"Heterogeneous Integration": Multi-function chips combining various semiconductor materials for enhanced performance in optoelectronics, sensing, and communication.
"Ultra-Low Power Electronics": Energy-efficient microchips minimizing power consumption, extending battery life for military sensors, wearables, and autonomous systems.
"Quantum Microelectronics": Quantum-enhanced sensors and communication devices using quantum principles for secure, sensitive military applications and advanced processing capabilities.
"SATCOM": Secure, encrypted satellite networks providing global, jam-resistant communication for military command and control in contested environments.
"Space-Based ISR": Satellites with imaging, radar, and infrared sensors for real-time intelligence, surveillance, and reconnaissance, offering persistent monitoring of strategic areas.
"Space Situational Awareness (SSA)": Tracking space debris and foreign objects to protect satellites and assess potential space threats.
"Launch Systems & Propulsion": Rapid launch capabilities and advanced propulsion systems for deploying satellites and enabling long-duration missions.
"Space-Based Positioning, Navigation & Timing (PNT)": Enhanced GPS accuracy and alternative systems for navigation in GPS-denied environments, ensuring reliable military operations.
"Counterspace, Awareness & Defense": Anti-satellite systems and counterspace operations to protect military assets and maintain space superiority.
"In-Space Manufacturing & Repair": On-orbit servicing and fabrication technologies to repair, refuel, and build satellites or components directly in space.
"Solar Power": Deployable solar panels and space-based solar systems providing sustainable, uninterrupted energy for remote military operations and bases.
"Energy Harvesting": Converting kinetic or thermal energy from soldiers, vehicles, or machinery into electricity for powering field equipment and wearables.
"Microgrids": Resilient, local energy networks integrating renewable sources and traditional generators for energy independence at military bases and forward operations.
"Advanced Battery Technologies": Solid-state batteries and ultra-capacitors offering high energy density, fast charging, and longer lifespans for military vehicles and equipment.
"Hydrogen Fuel Cells": Efficient, portable power sources for extended field operations and hydrogen-powered military vehicles with reduced fuel dependence.
"Waste-to-Energy Technologies": Converting organic waste into usable energy, reducing waste and enhancing self-sufficiency in military field operations and bases.
"Energy Storage & Distribution Systems": Grid-scale and mobile energy storage solutions for renewable energy resilience and reliable backup power during military missions.
"High-Performance Computing (HPC)": Powerful computing systems for simulating complex military scenarios, processing large datasets, and supporting real-time decision-making.
"AI & Machine Learning": AI-driven systems for autonomous operations, predictive analytics, and proactive strategies in battlefield decision-making and equipment maintenance.
"Edge Computing": Real-time data processing and AI applications deployed at the edge of the network for faster, low-latency decision-making in field operations.
"Cyber Defense & Zero-Trust": AI-enhanced systems for real-time detection and response to cyber threats, including zero-trust architectures for network security.
"Software-Defined Networking (SDN)": Dynamic control of military networks, enabling flexible, secure, and automated communication systems in rapidly changing environments.
"Cloud Computing & Data Management": Secure, scalable cloud platforms for data storage and collaboration, ensuring data sovereignty and efficient management of military operations.
"Wearable Interfaces": Augmented reality displays and tactile feedback suits providing real-time data, navigation, and enhanced situational awareness for soldiers in combat environments.
"Brain Computer Interfaces (BCI)": Enables direct neural control of machines, enhancing operational speed and cognitive performance through brain signals and neurofeedback systems.
"Voice-Activated Systems": Hands-free control of military equipment and communication devices via advanced voice recognition and natural language processing for multitasking during missions.
"Gesture-Based Systems": Motion sensors interpreting hand or body gestures to control drones, robots, or AR systems, providing intuitive, non-verbal command capabilities.
"Tactile & Haptic Feedback Systems": Devices that deliver tactile feedback for improved control of remote systems, enhancing precision in operating vehicles, drones, or robotic systems.
"Exoskeletons & Powered Wearables": Wearable systems that augment strength, endurance, and mobility, enabling soldiers to carry heavy equipment and prevent injuries during extended missions.
"Multi-Modal Interfaces": Integrates voice, gesture, and touch inputs for seamless control of multiple systems, adapting to user preferences and battlefield conditions.
"High-Power Microwave Systems ": Microwave Generation, EMP pulse weapons to disrupt electronic systems, Countermeasures to protect against HPM attacks
"Targeting and control systems": Precision Targeting for laser systems
"Laser Technologies": Laser systems, beam control, materials and components. 
"High-Energy Laser Weapons (HPL)": Powerful lasers that destroy or disable enemy missiles, aircraft, and vehicles with precision and minimal collateral damage.
"High-Power Microwave Weapons (HPM)": Emit microwaves to disrupt or destroy electronic systems, disabling enemy communications, radar, and electronics over wide areas.
"Particle Beam Weapons": Use streams of subatomic particles to damage targets at the molecular level, potentially intercepting missiles in space.
"Non-Lethal Directed Energy Weapons": Emit energy (like millimeter waves or sound) to deter, disperse, or incapacitate adversaries without causing permanent harm.
"Counter-UAS (cUAS)": Directed energy systems that detect, track, and neutralize hostile drones to protect military assets.
"Directed Energy for Missile Defense": Utilize directed energy to intercept and destroy missiles during flight, including hypersonic and boost-phase threats.
"Electronic Warfare w/ DE": Employ energy to jam or disrupt enemy communications and sensors, dominating the electromagnetic spectrum and supporting cyber operations.
"Defense": Hypersonic weapons and defense systems. (Missiles, Interceptors, Strategic Deterrence)
"Aircraft": Hypersonic Aircraft and spaceplanes
"Systems": Hypersonic lift systems, propulsion systems.
"Hypersonic Glide Vehicles": Vehicles boosted to high altitudes and then glide at hypersonic speeds toward targets with high maneuverability for rapid strikes.
"Hypersonic Cruise Missiles": Air-breathing missiles powered by scramjet engines, enabling sustained hypersonic flight within the atmosphere for precise, high-speed attacks.
"Advanced Propulsion Systems": Development of scramjet and combined-cycle engines to achieve and sustain hypersonic speeds efficiently across a wide range.
"Thermal Protection Systems": High-temperature materials and heat dissipation techniques designed to withstand extreme heat and protect hypersonic vehicles' structural integrity.
"Aerodynamics & Flight Control": Research and development of aerodynamic designs and guidance systems for stability and control at hypersonic speeds under extreme conditions.
"Advanced Materials & Structures": Utilizing lightweight, strong materials and structures to enhance performance and withstand stresses during hypersonic flight.
"Counter-Hypersonic Defense Systems": Technologies for early detection, tracking, and interception of hypersonic threats to neutralize incoming hypersonic vehicles effectively.
"Cybersecurity": Protect systems and networks from digital attacks. 
"Electronic Warfare": Use electromagnetic spectrum to sense, protect, and communicate
"Radar": Advanced radar technologies for detection, tracking, and imaging in various environments.
"Communications": Secure and reliable communication channels, especially in contested environments
"Wideband Sensing": Create sensors that operate across a broad range of frequencies to detect and counter advanced threats.
"Multi Intelligence (Multi-INT) Fusion": Integrating various intelligence sources to create a comprehensive, real-time operational picture for enhanced military decision-making.
"Cyber-Electromagnetic Activities (CEMA)": Combining cyber operations with electronic warfare to disrupt enemy electromagnetic spectrum use while securing friendly communications.
"Cybersecurity of Sensing Systems": Protecting sensor networks from cyber threats to ensure the integrity and availability of critical military data.
"Cyber-Physical System (CPS) Defense": Securing military cyber-physical systems against cyber attacks through infrastructure protection and anomaly detection.
"Advanced SIGINT": Intercepting and analyzing electronic signals to gather intelligence on adversaries, using AI for rapid data processing.
"AI-Driven Cyber Defense": Employing artificial intelligence to predict, detect, and autonomously respond to cyber threats in real time.
"Integrated ISR": Combining intelligence, surveillance, and reconnaissance data from multiple sources for persistent monitoring and enhanced situational awareness.
"Advanced GEOINT": Provides mapping, visualization, and spatial analysis tools to monitor terrain and infrastructure for military planning and operations.
"Sensor Management Software": Integrates and controls multiple ISR sensors to optimize data collection and provide a cohesive operational picture for situational awareness.
"Hyper- & Multi-Spectral Sensors": Capture data across multiple wavelengths for detailed environmental and material analysis.
"LiDAR & Ground-Penetrating Radar Sensors": Generate high-resolution, three-dimensional maps of terrain and structures; Detect underground structures, tunnels, or buried objects.
"Acoustic Sensors": Detect and track submarines and underwater activity using sound waves.
"Radio Frequency (RF) Sensors": Detect and analyze RF signals for communication intelligence.
"Web & Social Media Monitoring": Tools that track, analyze, and report on online content from websites, forums, blogs, and social media platforms for real-time intelligence.
"Open-Source GEOINT": Software that collects and analyzes satellite imagery, mapping data, and geospatial information for terrain analysis and situational awareness.
"Web Scraping & Aggregators": Tools that scan networks, devices, and internet-connected systems to identify vulnerabilities and map adversary infrastructure; Specialized platforms that gather open-source information from multiple databases, websites, and social media in one location for analysis.
"Metadata, Text & Document Analysis": Extracts metadata and analyzes publicly available documents to uncover hidden insights and infrastructure information; Analyzes large volumes of text data to extract keywords, topics, or patterns for intelligence purposes.
"Multimedia Analysis": Tools for analyzing images, videos, and audio files to extract intelligence and identify patterns or anomalies.
"Predictive & Pattern Recognition AI": Leverages AI for pattern recognition, predictive analysis, and automating large-scale data analysis to enhance decision-making.
"Relationship Mapping & Network Analysis": Visual tools that map connections between individuals, organizations, or networks to uncover hidden relationships or key targets.
"Cyber Threat Intelligence & Dark Web Monitoring": Tracks illicit activities on open and dark web sources for early warnings of adversary plans or cyber threats.
"Real-Time Monitoring": Tools providing real-time updates on events, crises, or evolving situations from open sources, enhancing situational awareness.
"Quantum Computing": Advanced computing for encryption, cyber defense, and solving complex military challenges beyond traditional computing capabilities.
"Quantum Sensing": Develops highly sensitive sensors for GPS-independent navigation, detecting underground or underwater assets, and precise field measurements.
"Quantum Communication": Enables secure, tamper-proof communication through quantum key distribution and global quantum networks for military data transmission.
"Quantum Radar & Imaging": Uses quantum entanglement for superior radar detection and high-resolution imaging of stealth objects and low-signature targets.
"Quantum Metrology": Ultra-precise timekeeping and field measurements enhance synchronization, reconnaissance, and surveillance in military systems.
"Quantum Materials": Develops advanced materials like superconductors and topological insulators for high-performance sensors, electronics, and resilient military systems.
"Quantum AI": Combines quantum computing with AI to accelerate decision-making, predictive modeling, and optimize quantum systems for defense applications.
"Bio-Inspired Materials": Adaptive camouflage and bio-mimetic surfaces that replicate biological organisms for concealment and enhanced performance.
"Biomaterials & Bioelectronics": Developing smart, bio-inspired materials and biocompatible electronics for advanced sensors, adaptive systems, and defense applications.
"Environmental Biotechnology": Using biology to address environmental challenges, such as bioremediation, biosensors, and sustainable solutions for military operations.
"Synthetic Biology": Engineering biological systems for applications like biomanufacturing, genetic engineering, and biofabrication to enhance defense capabilities and resilience.
"Big Data Analytics": Processes vast amounts of open-source data to discover patterns, correlations, and actionable intelligence insights.

For your response, here is a list of the **only** possible choices for "sub CTAs" that you **must** choose from (it must have the same letter casing):
- Human Performance Enhancement
- Regenerative Medicine
- Neurotechnology & Brain-Computer Interfaces
- 5G & Beyond Networks
- mmWave Technology
- Massive MIMO
- Mesh Networking
- Spectrum Sharing & Cognitive Radio
- THz Technology
- Nanomaterials
- Metamaterials
- Smart Materials
- Advanced Ceramics & Composites
- Graphene & 2D Materials
- High-Entropy Alloys
- Explainable AI (XAI)
- Autonomous Unmanned Vehicles & Systems
- Swarm Intelligence
- Cyber Defense AI
- Autonomous Weapons Systems
- Command & Control AI
- Multi-Domain Command and Control (MDC2)
- Interoperability Standards and Protocols
- Tactical Edge Networking
- Cyber-Physical Systems (CPS)
- Joint All-Domain Command and Control (JADC2)
- Resilient Network Architectures
- Edge Computing and Distributed Systems
- Radiation-Hardened Electronics
- Trusted Microelectronics
- Chip-Scale Atomic Clocks (CSACs)
- Advanced Packaging & Integration
- Heterogeneous Integration
- Ultra-Low Power Electronics
- Quantum Microelectronics
- SATCOM
- Space-Based ISR
- Space Situational Awareness (SSA)
- Launch Systems & Propulsion
- Space-Based Positioning, Navigation & Timing (PNT)
- Counterspace, Awareness & Defense
- In-Space Manufacturing & Repair
- Solar Power
- Energy Harvesting
- Microgrids
- Advanced Battery Technologies
- Hydrogen Fuel Cells
- Waste-to-Energy Technologies
- Energy Storage & Distribution Systems
- High-Performance Computing (HPC)
- AI & Machine Learning
- Edge Computing
- Cyber Defense & Zero-Trust
- Software-Defined Networking (SDN)
- Cloud Computing & Data Management
- Wearable Interfaces
- Brain Computer Interfaces (BCI)
- Voice-Activated Systems
- Gesture-Based Systems
- Tactile & Haptic Feedback Systems
- Exoskeletons & Powered Wearables
- Multi-Modal Interfaces
- High-Power Microwave Systems 
- Targeting and control systems
- Laser Technologies
- High-Energy Laser Weapons (HPL)
- High-Power Microwave Weapons (HPM)
- Particle Beam Weapons
- Non-Lethal Directed Energy Weapons
- Counter-UAS (cUAS)
- Directed Energy for Missile Defense
- Electronic Warfare w/ DE
- Defense
- Aircraft
- Systems
- Hypersonic Glide Vehicles
- Hypersonic Cruise Missiles
- Advanced Propulsion Systems
- Thermal Protection Systems
- Aerodynamics & Flight Control
- Advanced Materials & Structures
- Counter-Hypersonic Defense Systems
- Cybersecurity
- Electronic Warfare
- Radar
- Communications
- Wideband Sensing
- Multi Intelligence (Multi-INT) Fusion
- Cyber-Electromagnetic Activities (CEMA)
- Cybersecurity of Sensing Systems
- Cyber-Physical System (CPS) Defense
- Advanced SIGINT
- AI-Driven Cyber Defense
- Integrated ISR
- Advanced GEOINT
- Sensor Management Software
- Hyper- & Multi-Spectral Sensors
- LiDAR & Ground-Penetrating Radar Sensors
- Acoustic Sensors
- Radio Frequency (RF) Sensors
- Web & Social Media Monitoring
- Open-Source GEOINT
- Web Scraping & Aggregators
- Metadata, Text & Document Analysis
- Multimedia Analysis
- Predictive & Pattern Recognition AI
- Relationship Mapping & Network Analysis
- Cyber Threat Intelligence & Dark Web Monitoring
- Real-Time Monitoring
- Quantum Computing
- Quantum Sensing
- Quantum Communication
- Quantum Radar & Imaging
- Quantum Metrology
- Quantum Materials
- Quantum AI
- Bio-Inspired Materials
- Biomaterials & Bioelectronics
- Environmental Biotechnology
- Synthetic Biology
- Big Data Analytics

You can respond with at least 1 "sub CTA" but at most 2 "sub CTAs".
Do not make new "sub CTAs", do not shorten category names, do **not** assume new categories or "sub CTAs".
Respond **only** with the categories and do not include additional text such as "I would classify this incustry as:".
Do **not** use the company's information to create new "sub CTAs".

If the description does **not** fall in any category, simply respond with "NONE".
If you come up with only one category, your response format should be: CATEGORY.
If you come up with 2 categories, first respond with the category that is most applicable to the company's objective and in this format: CATEGORY1;CATEGORY2.
"""

    request_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/133.0.0.0"
    }

    def request_ollama(self, prompt: str) -> str | None:
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                headers={"Content-Type": "application/json"},
                data=json.dumps(
                    {
                        "model": "llama3.2:latest",
                        "prompt": prompt,
                        "stream": False,
                        "temperature": 0,
                        "top_k": 0,
                        "top_p": 1,
                    }
                ),
            )

            response_json = json.loads(response.text)
            actual_response: str = str(response_json["response"])
            return actual_response

        except requests.exceptions.RequestException as e:
            print("Error: ", e)
            print("Try to run `ollama serve` to start ollama local server")
            return None

    def summarize_website(self, website_URL: str, sentence_count: int) -> str | None:
        webscraping_prompt = f"""
I will give you the contents of a company's website to summarize into {sentence_count} sentence.
Use the company's objective, core business, and the overall domain of the company as the criteria for the summary.
Reply with only the summary and no additional text, do NOT focus on specific fundings or events they have, do NOT focus on how the website is built, if I provide no text to analyze respond with 'NONE':
"""
        website_URL = (
            "https://" + website_URL
            if not website_URL.startswith(("http://", "https://"))
            else website_URL
        )

        try:
            res = requests.get(website_URL, headers=self.request_headers, timeout=10)
        except requests.exceptions.RequestException:
            print(f"BAD URL: {website_URL}")
            return None

        soup = BeautifulSoup(res.content, "html.parser")
        content = soup.strings
        page_text = ""
        for text in content:
            if len(text) <= 2:
                continue
            if len(page_text) > self.max_webscraper_text_length:
                break
            page_text += text.strip() + " "

        response = self.request_ollama(webscraping_prompt + page_text)
        if response == "NONE":
            return None
        return response

    def create_sub_ctas(self, description: str) -> str | None:
        ollama_response: str | None = self.request_ollama(
            self.categorization_prmopt + description
        )
        if ollama_response is None:
            return None

        sub_ctas: list[str] = ollama_response.strip().split(";")
        sub_ctas = list(set(sub_ctas))

        verified_sub_ctas = ""
        for sub in sub_ctas:
            sub = sub.strip()
            if sub in CTAs_SubCTAs.SUBCTA_TO_CTA.keys():
                if len(verified_sub_ctas) > 0:
                    verified_sub_ctas += "; "
                verified_sub_ctas += sub

        if len(verified_sub_ctas) == 0:
            return None

        return verified_sub_ctas
