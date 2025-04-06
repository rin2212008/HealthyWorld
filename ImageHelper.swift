import SwiftUI

class ImageHelper {
    static func imageToData(_ image: Image) -> Data? {
        // Create a UIHostingController to render the SwiftUI Image
        let hostingController = UIHostingController(rootView: image)
        let size = hostingController.view.intrinsicContentSize
        hostingController.view.frame = CGRect(origin: .zero, size: size)
        
        // Create a renderer to convert the view to an image
        let renderer = UIGraphicsImageRenderer(size: size)
        let uiImage = renderer.image { context in
            hostingController.view.drawHierarchy(in: hostingController.view.bounds, afterScreenUpdates: true)
        }
        
        // Convert UIImage to Data
        return uiImage.jpegData(compressionQuality: 0.8)
    }
    
    static func dataToImage(_ data: Data) -> Image? {
        guard let uiImage = UIImage(data: data) else { return nil }
        return Image(uiImage: uiImage)
    }
} 