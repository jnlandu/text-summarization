'use client';

import {  useState, useEffect, useRef } from 'react';
import axios from 'axios';

import ProtectedRoute from '../components/ProtectedRoute';
import Header from '../components/Header';
import Welcome from '../components/Welcome';

import { IoMdSend } from "react-icons/io";
import { GrFormAttachment } from "react-icons/gr";
import { AiFillRobot } from "react-icons/ai";
import { FaUserCircle } from "react-icons/fa";


const Home = () => {
  // const { user, logout } = useContext(AuthContext);
  
  const [chatMessages, setChatMessages] = useState([]);
  const [message, setMessage] = useState("");
  const endOfMessagesRef = useRef(null);

  useEffect(() => {
   
    const fetchChatMessages = async () => {
      const storedToken = localStorage.getItem('token');
      if (storedToken) {
        try {

          const apiUrl = `${process.env.NEXT_PUBLIC_FASTAPI_API_URL}/chat` 
          const chatResponse = await axios.get(apiUrl, {
            headers: { Authorization: `Bearer ${storedToken}` },
          });
          setChatMessages(chatResponse.data.messages);
        } catch (error) {
          console.error('Fetching chat messages failed:', error);
        }
      }
    };
    fetchChatMessages();
  }, []);

  useEffect(() => {
    endOfMessagesRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chatMessages]);

  const handleSend = async () => {
    if (message.trim() !== "") {
      const storedToken = localStorage.getItem('token');
      if (storedToken) {
        try {
          const apiUrl = `${process.env.NEXT_PUBLIC_FASTAPI_API_URL}/chat`;
          const response = await axios.post(apiUrl, { content: message }, {
            headers: { Authorization: `Bearer ${storedToken}` },
          });
          setChatMessages([...chatMessages, { text: message, sender: 'user' }, { text: response.data.response, sender: 'bot' }]);
          setMessage("");
        } catch (error) {
          console.error('Sending message failed:', error);
        }
      }
    }
  };

  return (
    <ProtectedRoute>
  
        <Header/>
        
        <div className="container mt-5">
        <Welcome />
        <div className="mb-3  chat-container ms-3 me-3">
          <div className="">
            {chatMessages.map((msg, index) => (
              <div key={index} className={`d-flex ${msg.sender === 'user' ? 'justify-content-end' : 'justify-content-start'}`}>
                <span className={`${msg.sender === 'bot' ? 'me-2 mt-2' : 'mt-1'}`}>
                  {msg.sender === 'bot' ? <AiFillRobot size={24} /> : <FaUserCircle size={24} />}
                </span>
                <p className={`${msg.sender === 'user' ? 'ms-2 text-white text-justify' : ''}  me-1 mt-2 rounded`}>
                  {msg.text}
                </p>
              </div>
            ))}
            <div ref={endOfMessagesRef} />
          </div>
        </div>

      <div className="question-input d-flex align-items-center gap-1 border">
          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            className="form-control"
            placeholder="Type your message here..."
            rows="2"
          ></textarea>
          {/* Attachment Icon */}
          <input 
            type="file" 
            id="fileInput" 
            className="d-none" 
            onChange={handleFileUpload}
          />
            <label htmlFor="fileInput" className="text-secondary cursor-pointer" style={{userSelect: "none"}}>
            <a  href="#"
             onClick={handleFileUpload}
            >  <GrFormAttachment  size={30}/> </a>
            </label>
          
          {/* Send Button */}
          <button 
             onClick={handleSend} 
            //  className="btn btn-primary"
            className="btn send-btn"

          >
            <IoMdSend />
          </button>
        </div>
        {/* <Footer/> */}
      </div>
    </ProtectedRoute>
  );

  function handleFileUpload(e) {
    const file = e.target.files?.[0];
    if (file) {
      console.log("Selected file:", file.name);
      // Handle the file upload logic here
      const reader = new FileReader();
      reader.onload = (event) => {
        const fileContent = event.target?.result;
        if (fileContent) {
        console.log("File content:", fileContent);
        // Send the file content to the server or handle it as needed
        }
      };
      reader.readAsText(file);
    }
    }
};

export default Home;
