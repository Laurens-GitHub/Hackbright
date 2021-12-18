function Fruits() {
  const [fruits, setFruits] = React.useState([]);

  React.useEffect(() => {
    fetch('/api/fruits')
      .then(response => response.json())
      .then(result => {
        setFruits(result);
      });
  }, []);

// implementing useEffect with an empty array '[]);' prevents the fetch from
// making a request to our server over and over (an endless loop)
// the empty array is the second argument of useEffect (the first being our
// effect, A.K.A. function), and it basically tells React to do the effect just once.

  if (fruits.length === 0) {
    return <p>Loading...</p>;
  }

  // We can also use map to replace lines 21-25 for a little shorter code:
  // const fruitListItems = fruits.map((fruit) => {
  //   return (<li key={fruit.fruit_id}>{fruit.name}</li>);
  // });

  const fruitListItems = [];

  for (const fruit of fruits) {
    fruitListItems.push(<li key={fruit.fruit_id}>{fruit.name}</li>);
  }

  return <ul>{fruitListItems}</ul>;
}

ReactDOM.render(<Fruits />, document.querySelector('#root'));
