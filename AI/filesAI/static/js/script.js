

const j = document.querySelectorAll('.holders');
j.forEach(hold=>{
    hold.addEventListener('click',()=>{
    hold.style.width = "100vw"
   
    })
})

document.getElementById('homebtn').addEventListener('click',()=>{

  tabswitch(1)
})
document.getElementById('querrybtn').addEventListener('click',()=>{

   tabswitch(2)
})
document.getElementById('historybtn').addEventListener('click',()=>{
    tabswitch(3)
})
document.getElementById('morebtn').addEventListener('click',()=>{
  tabswitch(4)
})

function tabswitch(me){
    const g = document.querySelector('.homecontent')
    const h = document.querySelector('.toberemoved');
    const j = document.querySelector('.userinteraction');
    const k = document.querySelector('.inlineinput')
    const l = document.querySelector('.alsotoberemoved')
    const m = document.querySelector('.morecontent');
    const bottomhold = document.querySelector('.bottomhold');
    const outer_border = document.querySelector('.border')
    
    if (me ===1){
        g.style.display = "block";;
        h.style.display  = "none";
        j.style.display = "none"; 
        k.style.display = "none";
        l.style.display = 'none';
        m.style.display = 'none';
        bottomhold.classList.remove('ai-active')
    }
    if(me ===2 ){
        g.style.display = 'none'
        l.style.display = 'none';
        h.style.display  = "block";
        j.style.display = "flex"; 
        k.style.display = "flex";
        m.style.display = 'none';
        bottomhold.classList.add('ai-active')
        outer_border.classList.ad
    }
    if(me ==3){
         g.style.display = 'none'
        h.style.display  = "none";
        j.style.display = "none"; 
        k.style.display = "none";
        l.style.display = "block";
        m.style.display = 'none';
        bottomhold.classList.remove('ai-active')
    }
    if(me ===4){
        g.style.display = 'none'
        h.style.display  = "none";
        j.style.display = "none"; 
        k.style.display = "none";
        l.style.display = 'none';
        m.style.display = 'block';
        bottomhold.classList.remove('ai-active')
    }

}

document.getElementById('morerec').addEventListener('click',(()=>{
    const m = document.querySelector('.recommended');
    m.classList.toggle('moreon')
 }))

 const notesContainer = document.getElementById('notes-container');
 const addBtn = document.getElementById('add-btn');
 const noteText = document.getElementById('note-text');
 
 // Load and display notes when the page loads
 document.addEventListener('DOMContentLoaded', displayNotes);
 
 // Add note button event listener
 addBtn.addEventListener('click', setNotesToStorage);
 
 function getNotesFromStorage() {
     const notes = localStorage.getItem('notes');
     return notes ? JSON.parse(notes) : [];
 }
 
 function setNotesToStorage() {
     const notes = getNotesFromStorage();
     const newNote = {
         id: Date.now(),
         text: noteText.value
     };
 
     if (newNote.text.trim()) {
         notes.push(newNote);
         localStorage.setItem('notes', JSON.stringify(notes));
         console.log('Note added:', newNote);
         noteText.value = ''; // Clear the textarea
         displayNotes(); // Refresh the list of notes
     } else {
         alert('Please write something before adding a note.');
     }
 }
 
 function displayNotes() {
     const notes = getNotesFromStorage();
     notesContainer.innerHTML = '';
 
     notes.forEach((note) => {
         const noteElement = document.createElement('div');
         noteElement.classList.add('note');
         noteElement.innerHTML = `
             <p class='note-text'>${note.text}</p>
             <div class="note-buttons">
                 <button class="edit-btn" data-note-id="${note.id}">Edit</button>
                 <button class="delete-btn" data-note-id="${note.id}">Delete</button>
             </div>
         `;
 
         // Add event listeners for edit and delete buttons
         noteElement.querySelector('.edit-btn').addEventListener('click', () => editNote(note.id));
         noteElement.querySelector('.delete-btn').addEventListener('click', () => deleteNote(note.id));
 
         notesContainer.appendChild(noteElement);
     });
 }
 
 function editNote(noteId) {
     const notes = getNotesFromStorage();
     const noteToEdit = notes.find(note => note.id === noteId);
 
     if (noteToEdit) {
         noteText.value = noteToEdit.text;
         deleteNote(noteId); // Remove the old note so that the edited one can replace it
     }
 }
 
 function deleteNote(noteId) {
     let notes = getNotesFromStorage();
     notes = notes.filter(note => note.id !== noteId);
     localStorage.setItem('notes', JSON.stringify(notes));
     displayNotes();
 }
 
window.addEventListener('message', function(event) {
    if (event.data === 'loginSuccess') {
        alert('Login successful!');
        location.reload();  // Reload the page or update the UI
    }
});
setTimeout(() => {
    document.getElementById('login-btn').click();
}, 3000);

document.getElementById('login-btn').addEventListener('click', function() {
    // Calculate the width and height in pixels
    const width = screen.width * 0.5;  // 50% of the screen width
    const height = screen.height * 0.4;  // 40% of the screen height
    
    // Calculate the position of the popup
    const left = 0;
    const top = (screen.height - height) / 2;

    // Open the popup window with the calculated dimensions and position
    window.open('/login', 'Google Login', `width=${width},height=${height},top=${top},left=${left}`);
});
