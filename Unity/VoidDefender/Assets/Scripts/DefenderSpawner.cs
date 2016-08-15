using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class DefenderSpawner : MonoBehaviour {

	public Camera myCamera;
	//UI elements need their boxcollider size to be in pixels rather than world units

	public Text infoText;
	// Use this for initialization
	private GameObject parent;
	private DarkEnergyDisplay starDisplay;

	private GameObject defender;
	private GameObject despawnTarget;

	void Start()
	{
		starDisplay = GameObject.FindObjectOfType<DarkEnergyDisplay>();
		parent = GameObject.Find("Defenders");
		if (!parent)
		{
			parent = new GameObject("Defenders");//Organizes the defenders to avoid cluttering up the editor

		}
		infoText.text = "";

		
	}

	// Update is called once per frame
	void Update () {
		if (Input.GetMouseButtonDown(0))
		{
			//gets collider so we can sort through the different button presses
			Vector3 mousePos = Input.mousePosition;
			mousePos.z = 10;

			Vector3 screenPos = myCamera.ScreenToWorldPoint(mousePos);

			RaycastHit2D[] hits;
			
			hits = Physics2D.RaycastAll(screenPos, Vector2.zero);

			bool readyToSpawn = false;
			bool despawn = false;

			foreach (RaycastHit2D hit in hits)
			{
				//we check for what is underneath. We ignore projeciles and enemies
				//but if there is an empty space, we care, unless we're 
				if (hit.collider.tag == "PauseBlock")
				{
					//This is for an unimplemented feature
					return;
				}
				else if (hit.collider.tag == "Defender")
				{
					//we either skip spawning, or we use the despawn option
					despawn = CheckDespawn(hit.collider);
					readyToSpawn = despawn;
					
					break;//end the for loop if we find a Defender
					//skip everything if a defender is in there
				}
				else if (hit.collider.tag == "DefenderSpawn")
				{
					readyToSpawn = true;
				}
			}
			if (readyToSpawn)
			{
				OnMouseDownAlt(despawn);//We either don't spawn or we don't
			}
			
		}
	}

	bool CheckDespawn(Collider2D collider)
	{
		//checks if we are currently using the despawner
		defender = ButtonSpawn.selectedDefender;
		infoText.text = "Space already occupied.";
		if (defender.tag == "Despawner")
		{
			despawnTarget = collider.gameObject;
			infoText.text = "Unsummoning " + despawnTarget.GetComponent<Defender>().GetName() + ".";
			return true;
		}
		return false;

	}

	void OnMouseDownAlt(bool despawn  = false)//this will usually default to false
	{
		Vector2 rawPos = CalculateWorldPointOfMouseClick();//gets the basic position of the click and converts it
		Vector2 roundedPos = SnapToGrid(rawPos);
		defender = ButtonSpawn.selectedDefender;
		if (!defender)
		{
			return;
		}
		if (despawn)
		{
			Destroy(despawnTarget);
		}
		else if (defender.tag != "Despawner")//we don't want to place anything if Despawner is active
		{

			int defenderCost = defender.GetComponent<Defender>().starCost;//need to remember to get the component
			if (starDisplay.UseDarkEnergy(defenderCost) == DarkEnergyDisplay.Status.SUCCESS)
			{
				SpawnDefender(roundedPos, defender);//calls the defender
			}
			else
			{
				infoText.text = "Insufficient Dark Energy!";
			}
		}
		
	}

	void SpawnDefender(Vector2 roundedPos, GameObject defender)
	{
		Quaternion zeroRot = Quaternion.identity;
		GameObject newDefender = Instantiate(defender, roundedPos, zeroRot) as GameObject;

		infoText.text = "Summoning " + newDefender.GetComponent<Defender>().GetName();
		newDefender.transform.parent = parent.transform;
	}

	Vector2 SnapToGrid(Vector2 rawWorldPos)
	{
		float newX = Mathf.RoundToInt(rawWorldPos.x);
		float newY = Mathf.RoundToInt(rawWorldPos.y);
		return new Vector2(newX, newY);
	}

	Vector2 CalculateWorldPointOfMouseClick()
	{
		float mouseX = Input.mousePosition.x;
		float mouseY = Input.mousePosition.y;
		float distanceFromCamera = 10f;

		Vector3 weirdTriplet = new Vector3(mouseX, mouseY, distanceFromCamera);
		Vector2 worldPos = myCamera.ScreenToWorldPoint(weirdTriplet);

		return worldPos;
	}
}
