async function triggerAgent() {
  try {
    const res = await fetch("http://localhost:5000/run-agent");
    const data = await res.text();
    document.getElementById("response").innerText = data;
  } catch (error) {
    document.getElementById("response").innerText = "⚠️ Error connecting to agent.";
    console.error("Error:", error);
  }
}
