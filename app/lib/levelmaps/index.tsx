import { LoungeStatus } from "~/types";
import Level1Map from "./Level1";
import Level2Map from "./Level2";
import Level3Map from "./Level3";
import Level4Map from "./Level4";
import Level5Map from "./Level5";

const LEVELS = [
  (loungeStatus: LoungeStatus[]) => <Level1Map loungeStatus={loungeStatus} />,
  (loungeStatus: LoungeStatus[]) => <Level2Map loungeStatus={loungeStatus} />,
  (loungeStatus: LoungeStatus[]) => <Level3Map loungeStatus={loungeStatus} />,
  (loungeStatus: LoungeStatus[]) => <Level4Map loungeStatus={loungeStatus} />,
  (loungeStatus: LoungeStatus[]) => <Level5Map loungeStatus={loungeStatus} />,
];

export default LEVELS;
