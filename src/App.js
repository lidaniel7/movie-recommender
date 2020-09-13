import React, {Component} from 'react';
import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";
import axios from 'axios';




class App extends Component {
  constructor() {
    super()

    this.onSubmit = this.onSubmit.bind(this);
    this.onChangeMovie = this.onChangeMovie.bind(this);
    this.onChangeRating = this.onChangeRating.bind(this);

    this.state = {
      movie: '',
      rating: 0,
      list: []
    }
  }

  onChangeMovie(e) {
    this.setState({
      movie: e.target.value
    })
  }

  onChangeRating(e) {
    this.setState({
      rating: e.target.value
    })
  }

  async getRecommendations(obj) {
    axios.post('http://127.0.0.1:5000/recommendations/', obj)
      .then((res) => {
        return res.data
      })
      .then((res) => {
        this.setState({
          list: res,
        })
      })
  }

  componentDidUpdate(prevProps, prevState) {
    if (this.state.list !== prevState.list) {
      console.log(this.state.list)
      console.log("State has been updated!")
    }
  }


  onSubmit(e) {
    e.preventDefault();
    const obj = {
      movie_name: this.state.movie,
      user_rating: this.state.rating,
    }

    this.getRecommendations(obj)
  }


  render() {
    return (
      <div className="App">
        <form onSubmit={this.onSubmit}>
          <div className="form-row justify-content-center">
            <div className="col-4">
              <input 
                type="text" 
                className="form-control" 
                placeholder="Movie Name"
                onChange={this.onChangeMovie}
              />
            </div>
            <div className="col-1">
              <input 
                type="text" 
                className="form-control" 
                placeholder="Rating"
                onChange={this.onChangeRating}
              />
            </div>
            <button className="btn btn-primary" type="submit">Submit form</button>
          </div>
        </form>
        {/* <img src="http://image.tmdb.org/t/p/w185/rhIRbceoE9lR4veEXuwCC2wARtG.jpg"/> */}
      </div>
    );
  }
}

export default App;
