using UnityEngine;
using System.Collections;

public class Shredder : MonoBehaviour {

	//kills objects no longer on screen to free up memory
	void OnTriggerEnter2D(Collider2D collider)
	{
		Destroy(collider.gameObject);
	}
}
