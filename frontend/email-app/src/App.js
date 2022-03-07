import './App.css';
import axios from 'axios';
import Table from 'react-bootstrap/Table';
import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

const baseURL = "http://localhost:8000/emails/email/";

function TableRow(props) {
  return (
    <tr>
      <td class="breakWords">{props.value.to_field}</td>
      <td class="breakWords">{props.value.from_field}</td>
      <td>{props.value.date}</td>
      <td class="breakWords">{props.value.subject}</td>
      <td class="breakWords">{props.value.message_id}</td>

    </tr>
  )
}

function App() {
  const [emails, setEmails] = React.useState(null);

  React.useEffect(() => {
    axios.get(baseURL).then((response) => {
      setEmails(response.data);
    });
  }, []);

  if (!emails) return null;

  return (
    <div class="container">
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>To</th>
            <th>From</th>
            <th>Date</th>
            <th>Subject</th>
            <th>Message-ID</th>
          </tr>
        </thead>
        <tbody>
          {
            emails.map((email, index) =>
              <TableRow value={email} key={index}/>
            )
          }
        </tbody>
      </Table>
    </div>
  )
}

export default App;
