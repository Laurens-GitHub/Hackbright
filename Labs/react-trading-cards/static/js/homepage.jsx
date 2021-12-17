'use strict';

function Homepage() {
  return (
    <React.Fragment>
    <ul>
      <li>Welcome to the trading card site</li>
    </ul>
      <br />Go to cards <a href="/cards">page</a>
      <br /><img src="/static/img/balloonicorn.jpg" />
    </React.Fragment>);
}

ReactDOM.render(<Homepage />, document.querySelector('#app'));


// Go ahead and add the following content to the return value of Homepage.render:

// A welcome message to the user

// A link to the /cards page

// A nice, large image of Balloonicorn (the image is located at /static/img/balloonicorn.jpg)

// Remember — you can edit static/css/site.css if you’d like to add some additional styling to your homepage.

// Be sure to test out your new HTML and ensure that it works and looks nice.