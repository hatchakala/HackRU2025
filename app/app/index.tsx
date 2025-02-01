import { View } from "react-native";
import Level from "~/components/Level";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "~/components/ui/accordion";
import { Card } from "~/components/ui/card";
import { Text } from "~/components/ui/text";

export default function Example() {
  return (
    <Accordion
      type="single"
      collapsible
      className="w-full max-w-sm native:max-w-md"
    >
      {[4, 3, 2, 1].map((level) => {
        return <Level level={level} key={level} />;
      })}
    </Accordion>
  );
}
