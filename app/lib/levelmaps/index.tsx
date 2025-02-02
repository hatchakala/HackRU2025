import { LoungeStatus } from "~/types";
import Level1Map from "./Level1";
import Level2Map from "./Level2";

const LEVELS = [
  (loungeStatus: LoungeStatus[]) => <Level1Map loungeStatus={loungeStatus} />,
  (loungeStatus: LoungeStatus[]) => <Level2Map loungeStatus={loungeStatus} />,
];

export default LEVELS;
