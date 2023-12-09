// since this is a regular js file, we have to import React into the file to make sure the required functionality can be used
import React from 'react';
// a header bar that is at the top of the page that just provides information about what the website is
const Header = () => {
  return (
    <header className="bg-gray-900 text-white p-4">
      <div className="container mx-auto">
        <h1 className="text-3xl font-bold">Amazon Sentiment Analysis</h1>
      </div>
    </header>
  );
};

export default Header;