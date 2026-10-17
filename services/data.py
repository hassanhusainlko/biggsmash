SERVICES = {
    'strategic-advisory-perception-intelligence': {
        'title': 'Strategic Advisory & Perception Intelligence',
        'icon': '🧠',
        'summary': 'Data-backed campaign strategy, real-time sentiment analysis, crisis response, and micro-target perception mapping.',
        'intro': None,
        'items': [
            {
                'title': 'Political & Policy Campaign Strategy',
                'text': 'Data-backed campaign architecture, election strategy, and public policy translation for government bodies, political leaders, and public figures.',
            },
            {
                'title': 'Real-Time Sentiment Analysis',
                'text': '24/7 digital and media monitoring to map public opinion, track narratives, and anticipate emerging trends.',
            },
            {
                'title': 'Crisis & Reputation Management',
                'text': 'Rapid-response counter-narrative deployment, media containment, and real-time issue mitigation.',
            },
            {
                'title': 'Demographic & Perception Mapping',
                'text': 'Micro-target profiling to ensure messaging aligns with localized cultural, economic, and social nuances.',
            },
        ],
    },
    'large-scale-event-management': {
        'title': 'Large-Scale Event Management & Experiential Production',
        'icon': '🎪',
        'summary': 'End-to-end planning and execution of large-scale public, corporate, and government events.',
        'intro': 'Biggsmash Outreach specialises in conceptualising, planning, and executing seamless, end-to-end large-scale public, corporate, and business events.',
        'items': [
            {
                'title': 'Public & Government Megastructures',
                'text': 'Large-scale public rallies, state welfare launches, government summits, town halls, and citizen awareness conventions.',
            },
            {
                'title': 'Corporate & Business Events',
                'text': 'Annual corporate summits, product launches, global partner meets, stakeholder roundtables, and industry expos.',
            },
            {
                'title': 'Protocol, VVIP & Logistics Management',
                'text': 'Complete venue management, security liaisoning, delegate registration, VVIP protocol handling, and stage/AV infrastructure setup.',
            },
            {
                'title': 'Experiential On-Ground Activations',
                'text': 'Branded pavilions, interactive display zones, live-streaming setups, and broadcast-ready stage productions.',
            },
        ],
    },
    'mass-media-atl-advertising': {
        'title': 'Mass Media & Above-The-Line (ATL) Advertising',
        'icon': '📺',
        'summary': 'Print, broadcast, and PR campaigns that put your message in front of the right audiences at scale.',
        'intro': None,
        'items': [
            {
                'title': 'Print Media Advertising & PR',
                'text': 'Front-page placements, editorial op-eds, official press releases, and full coverage across national and regional newspaper networks.',
            },
            {
                'title': 'Electronic & Broadcast Media',
                'text': 'Television Commercial (TVC) production and booking, news channel debate strategy, panel placement, and radio campaign production/jingles.',
            },
            {
                'title': 'National & Regional PR Engine',
                'text': 'Media briefings, press conference management, journalist networking, and official spokesperson coaching.',
            },
        ],
    },
    'on-ground-btl-activations': {
        'title': 'On-Ground & Below-The-Line (BTL) Activations',
        'icon': '🚐',
        'summary': 'Outdoor branding, mobile LED vans, and grassroots field drives that take campaigns to the ground.',
        'intro': None,
        'items': [
            {
                'title': 'Outdoor Branding (OOH)',
                'text': 'High-impact billboard networks, transit media (bus, train, and auto wraps), gantry displays, and LED hoardings in high-footfall corridors.',
            },
            {
                'title': 'Field Campaigns & Mobile Vans',
                'text': 'Customized LED promotional vans, street plays (Nukkad Natak), field canvassing teams, and interactive voter/citizen registration kiosks.',
            },
            {
                'title': 'Grassroots Canvassing & Awareness Drives',
                'text': 'Multi-district outreach drives bringing institutional, social, and commercial programs directly to local communities.',
            },
        ],
    },
    'digital-media-creative-studio-web': {
        'title': 'Digital Media, Creative Studio & Web Infrastructure',
        'icon': '💻',
        'summary': 'Social media, performance marketing, creative design, and secure web infrastructure under one roof.',
        'intro': None,
        'items': [
            {
                'title': 'Social Media Management (SMM)',
                'text': 'End-to-end strategy, content calendar management, visual asset design, short-form video production (Reels, Shorts, digital ads), and trendjacking across Meta, X (Twitter), YouTube, and LinkedIn.',
            },
            {
                'title': 'Web & App Infrastructure',
                'text': 'Custom web portals, campaign landing pages, government policy dashboards, and secure web applications built for high traffic.',
            },
            {
                'title': 'Performance Marketing & Ad-Tech',
                'text': 'Search Engine Marketing (SEM), geo-fenced audience advertising, programmatic ad campaigns, and conversion-optimised digital funnels.',
            },
            {
                'title': 'Institutional Identity & Visual Design',
                'text': 'Brand guidelines, logo design, campaign collateral, infographics, and policy whitepapers.',
            },
        ],
    },
    'direct-tele-outreach-tech-operations': {
        'title': 'Direct Tele-Outreach & Tech Operations',
        'icon': '📞',
        'summary': 'In-house call centers, WhatsApp automation, and SMS/IVR campaigns for direct citizen outreach.',
        'intro': None,
        'items': [
            {
                'title': 'In-House Dedicated Call Center',
                'text': 'Customised inbound and outbound tele-calling units for voter/customer survey research, feedback collection, grievance tracking, and direct citizen outreach.',
            },
            {
                'title': 'WhatsApp Automation & Broadcasting',
                'text': 'Official WhatsApp API integration, verified green-tick messaging, interactive conversational bots, and rich-media mass broadcasts.',
            },
            {
                'title': 'SMS & Voice Campaigns',
                'text': 'Bulk promotional/transactional SMS, automated Interactive Voice Response (IVR) feedback calls, and outbound pre-recorded voice blasts.',
            },
        ],
    },
}

def get_all_services():
    return SERVICES

def get_service(slug):
    return SERVICES.get(slug)
