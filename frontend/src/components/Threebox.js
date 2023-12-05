/** since this is a regular js file, we have to import React into the file to make sure the required functionality can be used
 * axios is a library that allows for calling of rest APIs from the frontend 
 * */
import React, { useState } from 'react';
import axios from 'axios';

// declares state variables that can be set when there is change from the user, allows for easy modification
const ThreeTextBoxes = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [isFormSubmitted, setIsFormSubmitted] = useState(false);
  const [textBoxValues, setTextBoxValues] = useState({
    comments: '',
    title: '',
  });
  const [responseData, setResponseData] = useState(null);
  const [selectedValue, setSelectedValue] = useState(1);

  /**
   * Handles if there is a change in all three text boxes of the textboxes and stores it in a state variable 
   * @param {clickEvent} event when someone types in a textbox that event is passed to this function
   * @param {string} textBoxName this is the name of the textbox that is being modified by the user
   */
  const handleTextBoxChange = (event, textBoxName) => {
    setTextBoxValues({
      ...textBoxValues,
      [textBoxName]: event.target.value,
    });
  };

  /**
   * Handles if there is a change in the drodown element which takes in the rating for each Amazon review
   * @param {clickEvent} event takes in the event of a changing rating value 
   */
  const handleDropdownChange = (event) => {
    const newValue = Number(event.target.value);
    setSelectedValue(newValue);
  };

  /**
   * When the button for the form submission is pressed, this sends the data that was collected by the inital form 
   * and passes it to the backend python server with the axios library and takes the response and displays it 
   */
  const handleAllTextBoxesChange = async () => {
    /**
     * modifies the json that is being used to hold textbox values and set a loading variable to true in case the api call 
     * takes a long time 
    */
    const postData = { ...textBoxValues, Rating: selectedValue };
    setIsLoading(true);
    /**
     * a try block to make sure that if there are any errors it is caught
     * an axios post call is made as data has to be sent to the backend  
     * stores the response data and then makes sure that there is confirmation that the form is submitted
     */
    try {
      const response = await axios.post('http://127.0.0.1:5000/model_change', postData);
      setIsFormSubmitted(true);
      setResponseData(response.data);
    // a catch to see if there is an error in the axios call
    } catch (error) {
      console.error('Error submitting form:', error);
    // makes sure the loading screen is not shown anymore
    } finally {
      setIsLoading(false);
    }
  };

  /**
   * Changes the background color of the website 
   * @returns the background color of the website based on what is being displayed 
   * if the response data is positive, the background color is green
   * if the response data is neutral, the background color is yellow 
   * if the reponse data is negative, the backgorund color is red 
   * default color is gray
   */
  const getBackgroundColor = () => {
    if (isFormSubmitted) {
      switch (responseData) {
        case 'Positive':
          return 'bg-green-500'; 
        case 'Neutral':
          return 'bg-yellow-500';
        case 'Negative':
          return 'bg-red-500'; 
        default:
          return 'bg-gray-600'; 
      }
    }
    return 'bg-gray-600'; 
  };
  
  // all of the html that will render on the screen 
  return (
    // this is the container for this whole component which includes everything but the header bar, calls the function to 
    // change the background color if needed
    <div className={`flex flex-col items-center justify-center h-screen mt-0 ${getBackgroundColor()}`}>
    { // this code renders when the review is submitted and displays the result that is provided by the model
      // also clears out the variables that were populated with a back button that allows the user to go back to the form
    isFormSubmitted ? (
      <div className="bg-gray-900 p-16 rounded shadow-xl text-gray-300" style={{ boxShadow: '15px 9px 22px 0px rgba(0,0,0,0.24)' }}>
        <h1 className="whitespace-pre-wrap font-semibold text-5xl text-gray-300 w-full">{responseData}</h1>
        <div className="flex items-center justify-center mt-4">
          <button
            className="bg-teal-600 text-white text-2xl px-6 py-4 rounded mt-4 justify-center"
            onClick={() => {
              setIsFormSubmitted(false);
              setTextBoxValues({ comments: '', title: '' });
              setSelectedValue(1);
            }}
          >
            Back
          </button>
        </div>
      </div>
      ) : (
        /**
         * form that allows for the passing in of individual amazon reviews, contains different textboxes and a button to submit
         * Title - takes in the title of the review that you would like to pass in to be analyzed 
         * Rating - provides a dropdown that tells the rating you would like to give for the product 
         * Comment - the comment of the review that you would like to analyze
         */
        <form className="bg-gray-900 p-16 rounded shadow-xl max-w-lg w-full h-lg" style={{ boxShadow: '15px 9px 22px 0px rgba(0,0,0,0.24)' }}>
          <div className="mb-14">
            <label className="block text-4xl font-semibold mb-2 text-gray-300">Title</label>
            <input
              type="text"
              placeholder="Title"
              className="border rounded w-full py-2 px-3 bg-gray-800 text-gray-300 text-2xl"
              value={textBoxValues.title}
              onChange={(e) => handleTextBoxChange(e, 'title')}
            />
          </div>
          <div className="mb-14">
            <label className="block text-4xl font-semibold mb-2 text-white">Rating</label>
            <select
              className="border rounded w-full py-2 px-3 bg-gray-800 text-gray-300 text-2xl"
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
          <div className="mb-6">
            <h1 className="block text-4xl font-semibold mb-2 text-gray-300">Comments</h1>
            <textarea
              rows="8"
              placeholder="Comments"
              className="border rounded w-full py-2 px-3 bg-gray-800 text-gray-300 text-xl"
              value={textBoxValues.comments}
              onChange={(e) => handleTextBoxChange(e, 'comments')}
            />
          </div>
          <div className="flex items-center justify-center">
            <button
              type="button"
              className="bg-teal-600 text-white text-lg px-4 py-2  rounded"
              onClick={handleAllTextBoxesChange}
              disabled={isLoading}
            >
              {isLoading ? 'Submitting...' : 'Rate Review'}
            </button>
          </div>
        </form>
      )}
      { // code for the loading screen that shows up when the form is submitted
      isLoading && (
        <div className="fixed top-0 left-0 w-full h-full bg-opacity-50 bg-gray-500 flex items-center justify-center">
          <div className="loader ease-linear border-8 border-t-8 border-gray-200 h-32 w-32"></div>
        </div>
      )}
    </div>
  );
};

export default ThreeTextBoxes;
