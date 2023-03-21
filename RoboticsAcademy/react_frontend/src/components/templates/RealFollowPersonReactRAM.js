import * as React from "react";
import { Box } from "@mui/material";
import { ViewProvider } from "../../contexts/ViewContext";
import { ExerciseProvider } from "../../contexts/RAMRealFollowPersonExerciseContext";
import RAMRealFollowPersonExerciseContext from "../../contexts/RAMRealFollowPersonExerciseContext";
import MainAppBar from "../common/MainAppBar";
import View from "../common/View";
import { THEORY_URL } from "../../helpers/TheoryUrlGetter";
import RealFollowPersonExerciseView from "../views/RAM/RAMRealFollowPersonExerciseView";

function RealFollowPersonReactRAM() {
  return (
    <Box>
      <ViewProvider>
        <ExerciseProvider>
        <MainAppBar 
            exerciseName={" Real Follow Person RR"} 
            context={RAMRealFollowPersonExerciseContext}
          />
          <View
            url={THEORY_URL.RealFollowPerson}
            exerciseId={
              <RealFollowPersonExerciseView context={RAMRealFollowPersonExerciseContext} />
            }
          />
        </ExerciseProvider>
      </ViewProvider>
    </Box>
  );
}

export default RealFollowPersonReactRAM;
