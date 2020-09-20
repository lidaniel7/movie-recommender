import React, {Component} from 'react';
import axios from 'axios';

class Posters extends Component {
    constructor() {
        super()


        this.state = {
            list: []
        }
    }

    // retrieveLinks(movieList) {
    //     const obj = {
    //         movies: movieList
    //     }
    //     axios.post('http://localhost:5000/movielinks/', obj)
    //         .then((res) => {
    //             return res.data
    //         })
    //         .then((res) => {
    //             this.setState({
    //                 list: res
    //             })
    //         })
    // }

    componentDidMount() {
        const obj = {
            movies: this.props.list
        }
        axios.post('http://localhost:5000/movielinks/', obj)
            .then((res) => {
                return res.data
            })
            .then((res) => {
                this.setState({
                    list: res
                })
            })
    }

    render() {
        // let x = this.retrieveLinks(this.props.list)
        this.props.list.map((movie) => 
            console.log(movie)
        )
        const movies = this.state.list
        movies.map((movie) => 
            console.log("http://image.tmdb.org/t/p/w185" + movie)
        )
        return (
            movies.map((movie) =>
                <img src={"http://image.tmdb.org/t/p/w185" + movie}/>
                // console.log(movie)
            )
        )
    }
}

export default Posters