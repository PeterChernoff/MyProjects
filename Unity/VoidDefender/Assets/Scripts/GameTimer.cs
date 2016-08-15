using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class GameTimer : MonoBehaviour {
	public float levelSeconds = 20;//putting in a value for the sake of having one
	public AudioClip winMusic;

	private Slider uiSlider;
	//private float remainingTime;
	private LoseCollider loseCollider;
	private bool isEndOfLevel;
	private AudioSource audioSource;
	private LevelManager levelManager;
	private GameObject winText;
	private GameObject[] buttons;

	// Use this for initialization
	void Start () {
		levelManager = FindObjectOfType<LevelManager>();
		isEndOfLevel = false;//we only want to run win once
		uiSlider = GetComponent<Slider>();
		//remainingTime = startTime;
		loseCollider = GameObject.FindObjectOfType<LoseCollider>();
		// TODO figure out how to disable the buttons

		winText = GameObject.Find("Text Win");
		if (!winText)
		{
			Debug.LogWarning("Please Create You Win Object");
		}
		winText.SetActive(false);
	}
	
	// Update is called once per frame
	void Update () {
		if (Time.timeSinceLevelLoad < levelSeconds)
		{
			UpdateSlider();
		}
		else if (!isEndOfLevel)
		{
			
			isEndOfLevel = true;
			HandleWinCondition();
			
		}
	}

	void UpdateSlider()
	{
		uiSlider.value = 1 - (Time.timeSinceLevelLoad / levelSeconds);
	}
	void HandleWinCondition()
	{
		loseCollider.enabled = false;
		DestroyAllTaggedObjects();
		Spawner[] spawners = FindObjectsOfType<Spawner>() ;
		foreach (Spawner spawner in spawners)//disables the spawners
		{
			spawner.enabled = false;
		}

		winText.SetActive(true);

		if (winMusic)
		{ //if there is music attached
			//disable the other music. Since it's a singleton, there will always be one
			MusicManager otherMusic = GameObject.FindObjectOfType<MusicManager>();
			if (otherMusic)
			{
				otherMusic.GetComponent<AudioSource>().enabled = false;
			}
			

			audioSource = GetComponent<AudioSource>();
			audioSource.clip = winMusic;
			audioSource.volume = PlayerPrefsManager.GetMasterVolume();

			audioSource.loop = false;
			audioSource.Play();
		}
		
		//Debug.Log("You win!");
		Invoke("GoToNextLevel", audioSource.clip.length+0.5f);
	}
	void DestroyAllTaggedObjects()
	{

		GameObject[] killAttackers = GameObject.FindGameObjectsWithTag("destroyOnWin");

		foreach (GameObject enemy in killAttackers)
		{
			//kills all the enemies
			enemy.GetComponent<Health>().DestroyObject();
		}
	}
	void GoToNextLevel()
	{
		levelManager.LoadNextLevel();
	}
}
