import React, { useState, useEffect } from "react";
import axios from "axios";

const AudioList = () => {
  const [audioFiles, setAudioFiles] = useState([]);

  useEffect(() => {
    const fetchAudioFiles = async () => {
      const response = await axios.get("http://localhost:5000/files");
      setAudioFiles(response.data);
    };

    fetchAudioFiles();
  }, []);

  return (
    <div>
      <h2>Uploaded Audio Files:</h2>
      <ul>
        {audioFiles.map((file) => (
          <li key={file._id}>{file.originalname}</li>
        ))}
      </ul>
    </div>
  );
};

export default AudioList;
