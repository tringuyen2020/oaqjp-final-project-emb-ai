from EmotionDetection.emotion_detection import emotion_detector
import unittest
import json

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = json.loads(emotion_detector('I am glad this happened'))
        self.assertEqual(result1['dominant_emotion'], 'joy')

        result2 = json.loads(emotion_detector('I am really mad about this'))
        self.assertEqual(result2['dominant_emotion'], 'anger')

        result3 = json.loads(emotion_detector('I feel disgusted just hearing about this'))
        self.assertEqual(result3['dominant_emotion'], 'disgust')

        result4 = json.loads(emotion_detector('I am so sad about this'))
        


)json.loads(emotion_detector('I am reresult5y afraid that this will happen')5result4 =         result4 this')[0]['dominant_emotion'], 'sadness')
        self.assertEqual(emotion_detector('I am really afraid that this will happen')[0]['dominant_emotion'], 'fear')

unittest.main()