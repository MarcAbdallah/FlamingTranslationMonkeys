import imgGovind from "./img/govind.jpg"
import imgAdi from "./img/adi.JPG"
import imgMarc from "./img/marc.png"
import imgZach from "./img/zach.png"

const members = {
    govind: {
        id: 0,
        name: "Govind Joshi",
        job: "Full Stack Engineer",
        bio: 'My name is Govind Joshi. I will be a Junior CS Major at UTCS. I am interested in NLP, Neural Networks, Computer Graphics, and I enjoy tinkering with full stack technologies. I am also very passionate about music and am a composer, saxophonist, and guitarist.',
        linkedin: "https://www.linkedin.com/in/govind-joshi/",
        img: imgGovind
    },
    shruti: {
        id: 1,
        name: "Aditya Ojha",
        job: "Backend Engineer",
        bio: "Adi is a Junior in UT's Electrical and Computer Engineering Department. His interests span machine learning research, hardware-software co-design, and biomedical applications of AI. He is a avid Toastmaster and loves to watch anime and workout in his free time.",
        linkedin: "https://www.linkedin.com/in/adiojha/",
        img: imgAdi
    },
    rishi: {
        id: 2,
        name: "Marc Abdallah",
        job: "Backend Engineer",
        bio: "Marc Abdallah is a junior in biomedical engineering at the Univedrsity of Texas at Austin. Marc is focused on studying biomolecular and cellular engineering. He is also interested in machine learning and AI-assisted medicine.",
        linkedin: "https://www.linkedin.com/in/marc-abdallah-55a5a1191/",
        img: imgMarc
    },
    randall: {
        id: 3,
        name: "Zachary Smith",
        job: "Backend Engineer",
        bio: "Zachary is a junior at the University of North Texas in Denton. Zachary is attending his 5th hackathon, and wants to specialize in deep learning.",
        linkedin: "https://www.linkedin.com/in/zachary-smith-ba2763194/",
        img: imgZach
    }
}

// const blurb = {
//     title: "Track My Candidate",
//     text: "There is a wealth of information available about elections, public representatives, and congressional legislation, but the majority of the public is still ill-informed about its government. The issue with government and legislation is that it is stereotyped with an aura of being boring and verbose. It is easier to digest bite-sized videos and articles curated by media networks rather than doing your own research when the data is so difficult to access. What use is data if it is not easily accessible? Democracy is dependent on the well-informed opinions of the public, and thus, we have made it our responsibility to provide that information in a simple and accessible manner with Track My Candidate."
// };

export { members }