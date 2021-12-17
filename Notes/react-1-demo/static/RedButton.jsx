function RedButton(props) {
  return (
    <div>
      <button type="button" style={{backgroundColor: 'red', color: 'white'}}>
        {props.message}
      </button>
    </div>
  );
}

ReactDOM.render(<RedButton message="Click me" />, document.querySelector('#root'));
