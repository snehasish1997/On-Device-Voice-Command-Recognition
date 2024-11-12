import UIKit
import AVFoundation
import CoreML

class ViewController: UIViewController, AVAudioRecorderDelegate {
    
    var audioRecorder: AVAudioRecorder!
    let model = VoiceCommandModel()  // Load the Core ML model
    
    override func viewDidLoad() {
        super.viewDidLoad()
        requestMicrophonePermission()
    }
    
    func requestMicrophonePermission() {
        AVAudioSession.sharedInstance().requestRecordPermission { granted in
            if granted {
                // Permission granted
                self.setupAudioRecorder()
            } else {
                // Handle permission denial
            }
        }
    }
    
    func setupAudioRecorder() {
        let audioSession = AVAudioSession.sharedInstance()
        try? audioSession.setCategory(.record, mode: .default, options: .defaultToSpeaker)
        try? audioSession.setActive(true)
        
        let settings = [
            AVFormatIDKey: Int(kAudioFormatLinearPCM),
            AVSampleRateKey: 16000,
            AVNumberOfChannelsKey: 1,
            AVLinearPCMBitDepthKey: 16,
            AVLinearPCMIsFloatKey: false
        ] as [String : Any]
        
        audioRecorder = try? AVAudioRecorder(url: getFileURL(), settings: settings)
        audioRecorder.delegate = self
        audioRecorder.prepareToRecord()
    }
    
    func getFileURL() -> URL {
        let path = FileManager.default.temporaryDirectory.appendingPathComponent("recording.wav")
        return path
    }
    
    func startRecording() {
        audioRecorder.record()
    }
    
    func stopRecording() {
        audioRecorder.stop()
        processAudioFile()
    }
    
    func processAudioFile() {
        let audioFileURL = getFileURL()
        
        // Load audio and preprocess for model
        let mfccFeatures = extractMFCC(audioFileURL)  // Implement this function for MFCC extraction
        
        // Prediction using Core ML
        guard let prediction = try? model.prediction(input: mfccFeatures) else {
            print("Prediction failed")
            return
        }
        
        // Get recognized command
        let command = prediction.classLabel
        print("Recognized command: \(command)")
    }
}
