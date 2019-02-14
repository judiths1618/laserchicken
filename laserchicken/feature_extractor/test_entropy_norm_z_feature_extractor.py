import unittest

import numpy as np

from laserchicken.feature_extractor.entropy_norm_z_feature_extractor import EntropyNormZFeatureExtractor
from laserchicken.test_tools import create_point_cloud


class TestExtractEntropy(unittest.TestCase):
    def test_use_norm_z(self):
        x = y = np.array([0, 0, 0])
        z = np.array([2, 2, 2])
        normalized_z = np.array([3, 4, 5])
        point_cloud = create_point_cloud(x, y, z, normalized_z=normalized_z)
        neighborhood = [[0, 1, 2]]

        extractor = EntropyNormZFeatureExtractor()
        entropy = extractor.extract(point_cloud, neighborhood, None, None, None)

        self.assertNotAlmostEqual(entropy, 0)



