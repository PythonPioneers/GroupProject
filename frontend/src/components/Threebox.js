// ThreeTextBoxes.js
import React, { useState } from 'react';
import axios from 'axios';

const ThreeTextBoxes = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [isFormSubmitted, setIsFormSubmitted] = useState(false);
  const [textBoxValues, setTextBoxValues] = useState({
    ID: '',
    comments: '',
    title: '',
  });

  const [selectedValue, setSelectedValue] = useState(1);

  const handleTextBoxChange = (event, textBoxName) => {
    setTextBoxValues({
      ...textBoxValues,
      [textBoxName]: event.target.value,
    });
  };

  const handleDropdownChange = (event) => {
    const newValue = Number(event.target.value);
    setSelectedValue(newValue);
    console.log('Selected Dropdown Value:', newValue);
  };


  const handleAllTextBoxesChange = async () => {
    // Add your logic for handling changes in all text boxes and dropdown
    console.log('Text Box Values:', textBoxValues);
    console.log('Selected Dropdown Value:', selectedValue);

    const postData = { ...textBoxValues };

    postData.Rating = selectedValue

    setIsLoading(true);

    // Add logic for form submission
    try {
      const response = await axios.post('http://127.0.0.1:5000/model_change', postData);

      // Handle the response here
      console.log('Response:', response.data);
      console.log('Form submitted successfully:', response.data);
      setIsFormSubmitted(true);
    }  catch (error) {
    console.error('Error submitting form:', error);
  } finally {
    setIsLoading(false);
  }
  };

  const handleEmptyButtonClick = () => {
    // Empty event handler for the second button
  };

  return (
    <div className="flex items-center justify-center h-screen mt-0">
      {isFormSubmitted ? (
        <div>
          <h2>Form Submitted Successfully!</h2>
          {/* Render additional content or components for the success state */}
        </div>
      ) : (
      <form className="w-full max-w-sm">
        <div className="mb-4 w-96">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            ID
          </label>
          <input
            type="text"
            placeholder="ID"
            className="border rounded w-full py-2 px-3"
            value={textBoxValues.ID}
            onChange={(e) => handleTextBoxChange(e, 'ID')}
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Title
          </label>
          <input
            type="text"
            placeholder="Title"
            className="border rounded w-full py-2 px-3"
            value={textBoxValues.title}
            onChange={(e) => handleTextBoxChange(e, 'title')}
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Dropdown
          </label>
          <select
            className="border rounded w-full py-2 px-3"
            value={selectedValue}
            onChange={handleDropdownChange}
          >
            {[1, 2, 3, 4, 5].map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Comments
          </label>
          <textarea
            type="text"
            rows="4"
            placeholder="Comments"
            className="border rounded w-full py-2 px-3"
            value={textBoxValues.comments}
            onChange={(e) => handleTextBoxChange(e, 'comments')}
          />
        </div>
        <div className="flex items-center justify-center">
          <button
            type="button"
            className="bg-blue-500 text-white px-4 py-2 mr-2 rounded"
            onClick={handleAllTextBoxesChange}
            disabled={isLoading}
          >
            Submit Form
          </button>
        </div>
      </form>)}

      {/* Loading screen */}
      {isLoading && (
        <div className="fixed top-0 left-0 w-full h-full bg-opacity-50 bg-gray-500 flex items-center justify-center">
          <div className="loader ease-linear border-8 border-t-8 border-gray-200 h-32 w-32"></div>
        </div>
      )}
    </div>
  );
};

export default ThreeTextBoxes;
