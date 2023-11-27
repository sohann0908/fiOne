import React from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';

function form(){

    const handleClick = () => {
        fetch("")
        .then((res)=>res.json())
        .then(console.log(res));
    }

    return(
        <>
      <Container className="my-4">
        <h2>Add Card Details</h2>
      </Container>

      <hr className="featurette-divider my-4" />

      <Container>
        <Form>
          <Row className="g-3">
            <Col>
              <Form.Label htmlFor="cardnum">Card Number</Form.Label>
              <Form.Control type="number" id="cardnum" maxLength="16" placeholder="1234 xxxx xxxx xxxx" />
            </Col>
            <Col md={6}>
              <Form.Label htmlFor="expiry">Expiry</Form.Label>
              <Form.Control type="number" id="expiry" maxLength="4" placeholder="12/24" />
            </Col>
            <Col md={6}>
              <Form.Label htmlFor="cvv">CVV</Form.Label>
              <Form.Control type="number" id="cvv" maxLength="3" placeholder="123" />
            </Col>
            <Col>
              <Form.Label htmlFor="name">Name</Form.Label>
              <Form.Control type="text" id="name" placeholder="Paul John" />
            </Col>

            <Col md={6}>
              <Form.Check
                type="checkbox"
                id="flexCheckDefault"
                label="Save My Card"
              />
            </Col>
            <Col md={6}>
              <Form.Check
                type="checkbox"
                id="flexCheckChecked"
                label="Set As Priority Card"
              />
            </Col>

            <Col md={6}>
              <Button variant="primary" type="button" onClick={handleClick}>
                Submit
              </Button>
            </Col>
          </Row>
        </Form>
      </Container>
    </>
    )
}

export default form;