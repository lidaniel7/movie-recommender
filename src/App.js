import React, {Component} from 'react';
import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";
import axios from 'axios';
import Posters from './Posters.js';


class App extends Component {
  constructor() {
    super()

    this.onSubmit = this.onSubmit.bind(this);
    this.onChangeMovie = this.onChangeMovie.bind(this);
    this.onChangeRating = this.onChangeRating.bind(this);

    this.state = {
      movie: '',
      rating: 0,
      list: [],
      isSubmitted: false,
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


  // componentDidUpdate(prevProps, prevState) {
  //   if (this.state.isSubmitted !== prevState.isSubmitted) {
  //     this.setState({
  //       isSubmitted: false
  //     })
  //   }
  // }


  onSubmit(e) {
    e.preventDefault();
    const obj = {
      movie_name: this.state.movie,
      user_rating: this.state.rating,
    }

    axios.post('http://localhost:5000/recommendations/', obj)
      .then((res) => {
        return res.data
      })
      .then((res) => {
        this.setState({
          list: res,
          isSubmitted: true,
        })
      })
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
        {this.state.isSubmitted && <Posters list={this.state.list}/>}
      </div>
    );
  }
}

export default App;
