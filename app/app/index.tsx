import { useState } from "react";
import { View } from "react-native";
import Level from "~/components/Level";
import { Accordion } from "~/components/ui/accordion";

export default function App() {
  const [openLevel, setOpenLevel] = useState<number>(1);

  return (
    <View className="h-full">
      <Accordion
        type="single"
        collapsible
        className="w-full max-w-sm native:max-w-md"
        value={`${openLevel}`}
        onValueChange={(itemLevel) => setOpenLevel(parseInt(itemLevel || ""))}
      >
        {[4, 3, 2, 1].map((level) => {
          return (
            <Level level={level} key={level} isOpen={openLevel === level} />
          );
        })}
      </Accordion>
    </View>
  );
}
