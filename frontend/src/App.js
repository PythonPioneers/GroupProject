import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
} from "react-router-dom";
import ThreeTextBoxes from './components/Threebox';
import Header from './components/Header';

function App() {
  return (
    <div className="App">
        <Header/>
        <ThreeTextBoxes />
    </div>
  );
}

export default App;
