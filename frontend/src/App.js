import React from "react";
import AudioUploader from "./AudioUploader";
import AudioList from "./AudioList";

const App = () => {
  return (
    <div>
      <h1>Audio Uploader</h1>
      <AudioUploader />
      <AudioList />
    </div>
  );
};

export default App;
