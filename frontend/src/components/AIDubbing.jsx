import React, { Component } from 'react'

class AIDubbing extends Component {
    
    constructor() {
        super();
        // Defaults
        this.state = {
            selectedFile: null,
            selectedVid: null,
            targetLang: "fr",
            voice: "0", // female
            sync: "0", // No sync
        };
    
        this.onFileSelect = event => {
            this.setState({ selectedFile: event.target.files[0]});
        }

        this.oneVidSelect = event => {
            this.setState({ selectedVid: URL.createObjectURL(event.target.files[0]) })
        }

        this.onLangSelect = event => {
            this.setState({ targetLang: event.target.value});
        }

        this.onVoiceSelect = event => {
            this.setState({ voice: event.target.value })
        }

        this.onSyncChange = event => {
            this.setState({ sync: event.target.value })
        }
    
        this.onFileUpload = () => {
            // HTML Form Element
            if(this.state.selectedFile && this.state.selectedVid) {
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
                formData.append(
                    "sync",
                    this.state.sync
                )

                var audio = document.getElementById("speech");
                var video = document.getElementById("vid");
                video.src = this.state.selectedVid;

                formData.append(
                    "duration",
                    video.duration // seconds
                )

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
                    
                    // Mute and play video
                    audio.play();
                    video.muted = true;
                    video.play();
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
                    <label>Subtitles (SRT)</label>
                    <input type="file" onChange={this.onFileSelect} /><br />
                    <label>Video Path</label>
                    <input type="file" onChange={this.oneVidSelect} /><br />
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
                    </select><br />
                    <label>Sync Options</label>
                    <select name="sync" id="sync" onChange={this.onSyncChange}>
                        <option value="0">No Sync</option>
                        <option value="1">Ratio Sync</option>
                        <option value="2">Super Sync!</option>
                    </select>
                    <button onClick={this.onFileUpload}>
                      Upload!
                    </button>
                </div>
                {/* {this.getFileData()} */}
                <video controls width="800px" height="600px" id="vid" /><br/>
                <audio controls id="speech" />
            </div>
        )
    }
}

export default AIDubbing