import * as React from "react";
import { Box } from "@mui/material";
import { ViewProvider } from "../../contexts/ViewContext";
import { ExerciseProvider } from "../../contexts/RAMFollowPersonExerciseContext";
import RAMFollowPersonExerciseContext from "../../contexts/RAMFollowPersonExerciseContext";
import MainAppBar from "../common/MainAppBar";
import View from "../common/View";
import { THEORY_URL } from "../../helpers/TheoryUrlGetter";
import FollowPersonExerciseView from "../views/RAM/RAMFollowPersonExerciseView";

function FollowPersonReactRAM() {
  return (
    <Box>
      <ViewProvider>
        <ExerciseProvider>
          <MainAppBar 
            exerciseName={" Follow Person RR"} 
            context={RAMFollowPersonExerciseContext}
          />
          <View
            url={THEORY_URL.FollowPerson}
            exerciseId={
              <FollowPersonExerciseView context={RAMFollowPersonExerciseContext} />
            }
          />
        </ExerciseProvider>
      </ViewProvider>
    </Box>
  );
}

export default FollowPersonReactRAM;
