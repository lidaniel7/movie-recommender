import React, {Component} from 'react';
import axios from 'axios';

class Posters extends Component {
    constructor() {
        super()


        this.state = {
            list: []
        }
    }

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
    //load poster images of top 10 recommended movies
    render() {
        return (
            movies.map((movie) =>
                <img src={"http://image.tmdb.org/t/p/w185" + movie}/>
            )
        )
    }
}

export default Posters