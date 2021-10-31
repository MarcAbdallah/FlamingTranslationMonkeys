import React, { Component } from 'react'

class FileUpload extends Component {
    
    constructor() {
        super();
        // Defaults
        this.state = {
            selectedFile: null,
            targetLang: "fr",
            voice: 0 // female
        };
    
        this.onFileSelect = event => {
            this.setState({ selectedFile: event.target.files[0]});
        }

        this.onLangSelect = event => {
            this.setState({ targetLang: event.target.value});
        }

        this.onVoiceSelect = event => {
            this.setState({ voice: event.target.value })
        }
    
        this.onFileUpload = () => {
            // HTML Form Element
            if(this.state.selectedFile) {
                const formData = new FormData();
    
                formData.append(
                    "file",
                    this.state.selectedFile
                );
                formData.append(
                    "lang",
                    this.state.targetLang
                );
                formData.append(
                    "voice",
                    this.state.voice
                )

                var audio = document.getElementById("speech");
                var xhr = new XMLHttpRequest();
                xhr.open("POST", "http://localhost:8081/SRTtoAPI", true);
                //xhr.setRequestHeader('Content-Type', 'application/json');
                xhr.responseType = 'blob';
                xhr.onload = function () {
                    var blob = new Blob([xhr.response], {type: 'audio/wav'});
                    var objectUrl = URL.createObjectURL(blob);
                    audio.src = objectUrl;
                    // Release resource when it's loaded
                    audio.onload = function() {
                      URL.revokeObjectURL(objectUrl);
                    };
                    audio.play();
                }
                xhr.send(formData);
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
                    <select name="language" id="language" onChange={this.onLangSelect}>
                        <option value="fr">French</option>
                        <option value="hi">Hindi</option>
                        <option value="ar">Arabic</option>
                        <option value="en">English</option>
                    </select>
                    <select name="gender" id="gender" onChange={this.onVoiceSelect}>
                        <option value="0">Female</option>
                        <option value="1">Male</option>
                    </select>
                    <button onClick={this.onFileUpload}>
                      Upload!
                    </button>
                </div>
                {this.getFileData()}
                <audio controls id="speech" />
            </div>
        )
    }
}

export default FileUpload