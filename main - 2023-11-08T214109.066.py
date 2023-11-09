# Define a dictionary of land development terms
land_development_dictionary = {
    "Land Use": [
        "Residential",
        "Commercial",
        "Industrial",
        "Mixed-Use",
        "Agricultural",
    ],
    "Zoning": [
        "Residential Zone",
        "Commercial Zone",
        "Industrial Zone",
        "Agricultural Zone",
        "Special Use Zone",
    ],
    "Permit": [
        "Building Permit",
        "Zoning Permit",
        "Environmental Permit",
        "Land Use Permit",
        "Development Permit",
    ],
    "Infrastructure": [
        "Roads",
        "Utilities",
        "Sewer System",
        "Water Supply",
        "Electricity",
    ],
    "Surveying": [
        "Land Survey",
        "Topographic Survey",
        "Boundary Survey",
        "Site Plan",
        "Aerial Survey",
    ],
    "Environmental Impact": [
        "Environmental Assessment",
        "Environmental Impact Statement",
        "Ecological Assessment",
        "Conservation Area",
    ],
    "Architectural Design": [
        "Architectural Plans",
        "Site Design",
        "Landscape Design",
        "Building Layout",
    ],
    "Construction": [
        "Site Preparation",
        "Excavation",
        "Foundation",
        "Framing",
        "Finishing",
    ],
    "Landscaping": [
        "Planting",
        "Hardscape",
        "Irrigation",
        "Green Space",
        "Landscaping Design",
    ],
    "Regulations": [
        "Zoning Regulations",
        "Building Codes",
        "Environmental Regulations",
        "Safety Standards",
    ],
}

# Print the dictionary
for category, words in land_development_dictionary.items():
    print(f"{category}: {', '.join(words)}")

