import { View, StyleSheet } from 'react-native';

import Button from '@/components/Button';
import ImageViewer from '@/components/ImageViewer';

const PlaceHolderImage = require('@/assets/images/background-image.avif');

export default function Index() {
  return (
    < View style={styles.container} >
      <View style={styles.imageContainer}>
        <ImageViewer imgSource={PlaceHolderImage} />
      </View>

      <View style={styles.footerContainer}>
        <Button label="get video feed" />
        <Button label="get sensor info" />
      </View>
    </View >


  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#25292e',
    alignItems: 'center',

  },
  ImageContainer: {
    flex: 1,
  },
  footerContainer: {
    flex: 1 / 3,
    alignItems: 'center',
  },
}); 
