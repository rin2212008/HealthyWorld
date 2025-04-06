import Foundation

struct Resource: Identifiable {
    let id = UUID()
    let name: String
    let type: ResourceType
    let address: String
    let distance: String
    let rating: Double
    let description: String
    let phone: String
    let website: String?
    
    enum ResourceType: String {
        case therapy = "Therapy"
        case seminar = "Trauma Seminar"
        case hospital = "Hospital"
        case supportGroup = "Support Group"
        case wellnessCenter = "Wellness Center"
    }
}

// Sample data
extension Resource {
    static let sampleResources: [Resource] = [
        Resource(
            name: "Mindful Healing Center",
            type: .therapy,
            address: "123 Wellness Ave, San Francisco",
            distance: "0.5 miles",
            rating: 4.8,
            description: "Specialized in trauma therapy and mental health counseling",
            phone: "(555) 123-4567",
            website: "www.mindfulhealing.com"
        ),
        Resource(
            name: "Healing Through Trauma Workshop",
            type: .seminar,
            address: "456 Recovery St, San Francisco",
            distance: "1.2 miles",
            rating: 4.9,
            description: "Weekly trauma healing workshops and group sessions",
            phone: "(555) 234-5678",
            website: "www.traumaworkshop.com"
        ),
        Resource(
            name: "San Francisco General Hospital",
            type: .hospital,
            address: "789 Medical Blvd, San Francisco",
            distance: "2.1 miles",
            rating: 4.5,
            description: "24/7 emergency services and mental health support",
            phone: "(555) 345-6789",
            website: "www.sfgh.org"
        ),
        Resource(
            name: "Community Support Network",
            type: .supportGroup,
            address: "321 Unity Lane, San Francisco",
            distance: "0.8 miles",
            rating: 4.7,
            description: "Daily support groups for various mental health needs",
            phone: "(555) 456-7890",
            website: "www.communitysupport.org"
        ),
        Resource(
            name: "Holistic Wellness Center",
            type: .wellnessCenter,
            address: "654 Balance Rd, San Francisco",
            distance: "1.5 miles",
            rating: 4.6,
            description: "Comprehensive wellness services including yoga and meditation",
            phone: "(555) 567-8901",
            website: "www.holisticwellness.com"
        )
    ]
} 