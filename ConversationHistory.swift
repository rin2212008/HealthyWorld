import Foundation

class ConversationHistory: ObservableObject {
    @Published var entries: [ConversationEntry] = []
    @Published var currentMood: Int = 0
    
    struct ConversationEntry: Identifiable {
        let id = UUID()
        let text: String
        let isUser: Bool
        let sentimentScore: Int
        let timestamp: Date
    }
    
    init() {
        // Add some initial entries to show the mood meter working
        addEntry(text: "Hello", isUser: true, sentimentScore: 5)
        addEntry(text: "I'm feeling good today", isUser: true, sentimentScore: 10)
        addEntry(text: "The weather is nice", isUser: true, sentimentScore: 5)
    }
    
    func addEntry(text: String, isUser: Bool, sentimentScore: Int) {
        let entry = ConversationEntry(text: text, isUser: isUser, sentimentScore: sentimentScore, timestamp: Date())
        entries.append(entry)
        updateCurrentMood()
    }
    
    private func updateCurrentMood() {
        // Consider only the last 10 entries for mood calculation
        let recentEntries = entries.suffix(10)
        let totalScore = recentEntries.reduce(0) { $0 + $1.sentimentScore }
        currentMood = totalScore / max(1, recentEntries.count)
        
        // Ensure mood stays within reasonable bounds (-50 to 50)
        currentMood = max(-50, min(50, currentMood))
    }
} 