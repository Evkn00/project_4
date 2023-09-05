<script>
// Generate the "Gender" dropdown options with D3.js
const genderOptions = ['Male', 'Female', 'Other'];

d3.select('#gender')
    .selectAll('option')
    .data(genderOptions)
    .enter()
    .append('option')
    .text(d => d)
    .attr('value', d => d);

// Generate the "Age" dropdown options with D3.js
const ageOptions = Array.from({ length: 100 }, (_, i) => i + 1);

d3.select('#age')
    .selectAll('option')
    .data(ageOptions)
    .enter()
    .append('option')
    .text(d => d)
    .attr('value', d => d);

// Generate the "Hypertension" dropdown options with D3.js
const hypertensionOptions = ['No', 'Yes'];

d3.select('#hypertension')
    .selectAll('option')
    .data(hypertensionOptions)
    .enter()
    .append('option')
    .text(d => d)
    .attr('value', d => d);

// Generate the "heart_disease" dropdown options with D3.js
const heart_diseaseOptions = ['No', 'Yes'];

d3.select('#heart_disease')
    .selectAll('option')
    .data(heart_diseaseOptions)
    .enter()
    .append('option')
    .text(d => d)
    .attr('value', d => d);

// Generate the "ever_married" dropdown options with D3.js
const ever_marriedOptions = ['No', 'Yes'];

d3.select('#ever_married')
    .selectAll('option')
    .data(ever_marriedOptions)
    .enter()
    .append('option')
    .text(d => d)
    .attr('value', d => d);

// Generate the "work_type" dropdown options with D3.js
const work_typeOptions = ['Private', 'Self-employed', 'children', 'govt_job', 'Never_worked'];

d3.select('#work_type')
    .selectAll('option')
    .data(work_typeOptions)
    .enter()
    .append('option')
    .text(d => d)
    .attr('value', d => d);            

// Generate the "Residence_type" dropdown options with D3.js
const Residence_typeOptions = ['Urban', 'Rural'];

d3.select('#Residence_type')
    .selectAll('option')
    .data(Residence_typeOptions)
    .enter()
    .append('option')
    .text(d => d)
    .attr('value', d => d);            
    
// Generate the "smnoking_status" dropdown options with D3.js
const smoking_statusOptions = ['Smokes currently', 'Formerly smoked', 'Never smoked', 'Unknown'];

d3.select('#smoking_status')
    .selectAll('option')
    .data(smoking_statusOptions)
    .enter()
    .append('option')
    .text(d => d)
    .attr('value', d => d);    

function submitForm() {
    // Collect user input data
    const data = {
        gender: document.getElementById('gender').value,
        age: document.getElementById('age').value,
        hypertension: document.getElementById('hypertension').value,
        heart_disease: document.getElementById('heart_disease').value,
        ever_married: document.getElementById('ever_married').value,
        work_type: document.getElementById('work_type').value,
        residence_type: document.getElementById('Residence_type').value,
        avg_glucose_level: document.getElementById('avg_glucose_level').value,
        smoking_status: document.getElementById('smoking_status').value
    };
    console.log(data);

    // Send the data to the API 
    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        // Display the prediction
        const prediction = result.prediction.prediction;
        console.log(prediction)
        document.getElementById('result').innerHTML = `Predicted Outcome: ${prediction}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

</script>