import React, { useEffect, useRef } from "react";
import { View, Animated, Easing, Dimensions } from "react-native";

const { width, height } = Dimensions.get("window");
const CIRCLE_SIZE = 10;
const BOUNDARY_PADDING = -1101; // Space around the screen to keep circles inside

const getRandomDirection = () => ({
  x: (Math.random() - 0.5) * 2, // Random direction: -1 to 1
  y: (Math.random() - 0.5) * 2,
});

const AnimatedCircles = () => {
  const circle1 = useRef(new Animated.ValueXY({ x: 0, y: 0 })).current;
  console.log(Dimensions.get("window"));

  useEffect(() => {
    const moveCircle = (circle: Animated.ValueXY) => {
      const move = () => {
        const direction = getRandomDirection();
        const currentPos = circle.__getValue(); // Get current position

        let newX = currentPos.x + direction.x * 100;
        let newY = currentPos.y + direction.y * 100;

        // Constrain within boundaries
        newX = Math.max(
          BOUNDARY_PADDING,
          Math.min(newX, width - CIRCLE_SIZE - BOUNDARY_PADDING)
        );
        newY = Math.max(
          BOUNDARY_PADDING,
          Math.min(newY, height - CIRCLE_SIZE - BOUNDARY_PADDING)
        );

        Animated.timing(circle, {
          toValue: { x: newX, y: newY },
          duration: 1000,
          easing: Easing.linear,
          useNativeDriver: false,
        }).start(() => move()); // Call recursively
      };
      move();
    };

    moveCircle(circle1);
  }, []);

  return (
    <View>
      <Animated.View
        style={[
          styles.circle,
          {
            backgroundColor: "red",
            transform: circle1.getTranslateTransform(),
          },
        ]}
      />
    </View>
  );
};

const styles = {
  circle: {
    width: CIRCLE_SIZE,
    height: CIRCLE_SIZE,
    borderRadius: CIRCLE_SIZE / 2,
    position: "absolute",
  },
};

export default AnimatedCircles;
