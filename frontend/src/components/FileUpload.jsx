import React, { Component } from 'react'
import axios from 'axios'

class FileUpload extends Component {
    
    constructor() {
        super();
        this.state = {
            selectedFile: null,
            targetLang: null
        };
    
        this.onFileSelect = event => {
            this.setState({ selectedFile: event.target.files[0]});
        }
    
        this.onFileUpload = () => {
            // HTML Form Element
            if(this.selectedFile && this.targetLang) {
                const formData = new FormData();
    
                formData.append(
                    this.props.file,
                    this.state.selectedFile,
                    this.state.selectedFile.name,
                    this.targetLang
                );
        
                axios.post("localhost:8081/SRTtoAPI/", formData);
            }
        };
    
        this.getFileData = () => {
            if (this.state.selectedFile) {
                return (
                    <div>
                        <h2>File Details:</h2>
                        <p>File Name: {this.state.selectedFile.name}</p>
                        <p>File Type: {this.state.selectedFile.type}</p>
                        <p>File Size: {this.state.selectedFile.size}</p>
                        <p>Last Modified: {this.state.selectedFile.lastModified}</p>
                    </div>
                )
            } else {
                return (
                    <div>
                        <h4>Select a file!</h4>
                    </div>
                )
            }
        }
    }

    render() {
        return (
            <div>
                <h3>Upload {this.props.file}</h3>
                <div>
                    <input type="file" onChange={this.onFileSelect} />
                    <label>Target</label>
                    <select name="language" id="language">
                        <option value="en">English</option>
                        <option value="fr">French</option>
                        <option value="hi">Hindi</option>
                        <option value="ar">Arabic</option>
                    </select>
                    <select name="gender" id="gender">
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                    </select>
                    <button onClick={this.onFileUpload}>
                      Upload!
                    </button>
                </div>
                {this.getFileData()}
            </div>
        )
    }
}

export default FileUpload