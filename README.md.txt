!!! Parola administratorului este abcd !!!

Am folosit 4 template-uri pe langa cel de baza:
    -in _base.html am facut navbar-ul cu functiile sale:
        -gallery, login si about me cand adminul nu este logat;
        -gallery, upload, logout si about me cand adminul este logat.
    -in index.html am afisat imaginile care au fost uploadate, expuse pe categorii. Langa fiecare imagine exista un buton de delete care sterge imaginea respectiva.
    -in login.html am creat formularul de login. Deoarece doar un singur utilizator are mai multe functii (adminul), nu am mai folosit si un camp de username. Dupa ce adminul se logheaza, acesta este redirectionat catre pagina de upload.
    -in upload.html am creat formularul de upload cu 3 campuri:
        -un camp pentru fisier;
        -un camp optional pentru redenumirea imaginii;
        -un camp pentru categorie.
    -fisierele suportate sunt de tip png, jpg, jpeg si webp. Dupa ce o imagine este incarcata, adminul este redirectionat catre galerie pentru a vedea rezultatul.
Pe partea de backend am avut nevoie de urmatoarele librarii:
    -os, pentru a lucra cu fisiere si directoare, de exemplu, la delete folosesc os.remove(image_path) pentru a sterge imaginea si os.rmdir(category) pentru a sterge o categorie goala
    -secure_filename din werkzeug.utils, pentru a elimina simbolurile din noul nume al fisierelor, astfel, imaginea poate fi salvata intr-un sistem de fisiere;
    -din flask am avut nevoie de urmatoarele:
        -session, pentru implementarea functionalitatii de login;
        -send_from_directory, pentru a afisa o imagine in dimensiunile ei originale atunci cand dau click pe ea;
        -request, pentru a prelua date din formulare
        -render_template, pentru a afisa template-urile
        -redirect, pentru a redirectiona utilizatorul in anumite situatii, de exemplu, dupa ce administratorul se logheaza, acesta este redirectionat la pagina de upload;
        -url_for, pentru a obtine path-ul pentru o imagine atunci cand o afisez sau pentru functionalitatea de delete.
In requirements.txt am pus Flask, Werkzeug si Jinja2.