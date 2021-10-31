import imgGovind from "./img/govind.jpg"
import imgShruti from "./img/shruti.JPG"
import imgRishi from "./img/rishi.jpg"
import imgRandall from "./img/randall.jpg"

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
        name: "Shruti Banerjie",
        job: "Backend Engineer",
        bio: "Shruti is a junior studying Computer Science at UT Austin. She is originally from Houston, Texas and is interested in Artificial Intelligence and Human-computer interaction. Shruti enjoys baking, painting, and watching movies in her free time. ",
        linkedin: "",
        img: imgShruti
    },
    rishi: {
        id: 2,
        name: "Rishi Iyer",
        job: "Backend Engineer",
        bio: "Rishi is a super-duper-senior who’s attending UT Austin part time to complete his BS in CS degree. He’s also an associate product manager for Kwanzoo, a B2B SaaS startup in the Bay Area. In his free time he enjoys hiking, biking, dance, and NBA basketball.",
        linkedin: "",
        img: imgRishi
    },
    randall: {
        id: 3,
        name: "Randall Crawford",
        job: "Frontend Engineer",
        bio: "Randall is a student at the University of Texas at Austin studying Computer Science. He is proficient in Java, Python, and C. In his free time, he enjoys wakeboarding, climbing, and strategy games.",
        linkedin: "",
        img: imgRandall
    }
}

const blurb = {
    title: "Track My Candidate",
    text: "There is a wealth of information available about elections, public representatives, and congressional legislation, but the majority of the public is still ill-informed about its government. The issue with government and legislation is that it is stereotyped with an aura of being boring and verbose. It is easier to digest bite-sized videos and articles curated by media networks rather than doing your own research when the data is so difficult to access. What use is data if it is not easily accessible? Democracy is dependent on the well-informed opinions of the public, and thus, we have made it our responsibility to provide that information in a simple and accessible manner with Track My Candidate."
};

export { blurb, members }