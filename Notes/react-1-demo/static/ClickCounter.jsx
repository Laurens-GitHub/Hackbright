function ClickCounter(props) {
  const [currentCount, setCurrentCount] = React.useState(props.initialCount);
  return (
    <div>
      <div>{currentCount}</div>
      <button type="button" onClick={() => setCurrentCount(currentCount + 1)}>
        Click me to increase the count
      </button>
    </div>
  );
}

ReactDOM.render(<ClickCounter initialCount={10} />, document.querySelector('#root'));
