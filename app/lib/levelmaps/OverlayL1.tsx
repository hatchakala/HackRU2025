import { View } from "react-native";
import OverlayItem from "~/components/OverlayItem";
import { LoungeStatus } from "~/types";

interface Overlay {
  levelStatus: LoungeStatus[];
}

const OverlayL1: React.FC<Overlay> = ({ levelStatus }) => {
  return (
    <View>
      <OverlayItem loungeStatus={levelStatus[0]} x={-130} y={150} />;
      <OverlayItem loungeStatus={levelStatus[1]} x={-130} y={100} />;
      <OverlayItem loungeStatus={levelStatus[2]} x={-130} y={70} />;
      <OverlayItem loungeStatus={levelStatus[3]} x={-95} y={30} />;
      <OverlayItem loungeStatus={levelStatus[4]} x={-15} y={35} />;
      <OverlayItem loungeStatus={levelStatus[5]} x={85} y={35} />;
      <OverlayItem loungeStatus={levelStatus[6]} x={100} y={75} />;
      <OverlayItem loungeStatus={levelStatus[7]} x={100} y={100} />;
      <OverlayItem loungeStatus={levelStatus[8]} x={100} y={125} />;
      <OverlayItem loungeStatus={levelStatus[9]} x={100} y={160} />;
      <OverlayItem loungeStatus={levelStatus[9]} x={60} y={100} />;
    </View>
  );
};

export default OverlayL1;
