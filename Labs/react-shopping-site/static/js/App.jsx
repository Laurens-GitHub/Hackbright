function App() {
  const [melons, setMelons] = React.useState({});
  const [shoppingCart, setShoppingCart] = React.useState({});

  React.useEffect(() => {
    fetch('/api/melons')
      .then(response => response.json())
      .then(result => setMelons(result)
      );
  }, []);


  function addMelonToCart(melonCode) {
    setShoppingCart((shoppingCart) => {
      const newShoppingCart = Object.assign({}, shoppingCart);

      // code to update cart here
      if (newShoppingCart.hasOwnProperty(melonCode)) {
        newShoppingCart[melonCode]++;

      } else {
        newShoppingCart.melonCode = melonCode;
      }
      console.log(shoppingCart)
      return newShoppingCart;
    })
  }

  // ...


  return (
    <ReactRouterDOM.BrowserRouter>
      <Navbar logo="/static/img/watermelon.png" brand="Ubermelon" />
      <div className="container-fluid">

        <ReactRouterDOM.Route exact path="/">
          <Homepage />
        </ReactRouterDOM.Route>

        <ReactRouterDOM.Route exact path="/shop">
          <AllMelonsPage melons={melons} addMelonToCart={addMelonToCart}/>
        </ReactRouterDOM.Route>

        <ReactRouterDOM.Route exact path="/cart">
          <ShoppingCartPage shoppingCart={shoppingCart} melons={melons}/>
        </ReactRouterDOM.Route>

      </div>
    </ReactRouterDOM.BrowserRouter>
  );
};

ReactDOM.render(<App />, document.querySelector('#root'));
