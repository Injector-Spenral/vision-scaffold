import unittest
import cv2
from vision import Vision


class VisionTests(unittest.TestCase):
    def test_sample_images(self):
        f = open("./tests/results.csv", "r")
        lines = f.read().split("\n")
        f.close()
        for line in lines[1:]:
            values = line.split(",")  # Filename.jpg, 1, 2
            results = camera_server.get_image_values(cv2.imread(f"./tests/{values[0]}"))
            for i in range(1, len(values)):
                self.assertAlmostEqual(results[i-1], float(values[i]))


if __name__ == "__main__":
    camera_server = Vision(test=True)
    unittest.main()
